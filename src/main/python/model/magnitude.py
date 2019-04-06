import logging
import math

from matplotlib.gridspec import GridSpec

from model.limits import Limits, LimitsDialog, ValuesDialog, dBRangeCalculator
from model.preferences import GRAPH_X_AXIS_SCALE, GRAPH_X_MIN, GRAPH_X_MAX

logger = logging.getLogger('magnitude')

SINGLE_SUBPLOT_SPEC = GridSpec(1, 1).new_subplotspec((0, 0), 1, 1)


class AxesManager:
    def __init__(self, data_provider, axes, fill_curves, fill_alpha, normalise_x=True):
        self.__provider = data_provider
        self.__axes = axes
        self.__fill_curves = fill_curves
        self.__fill_alpha = fill_alpha
        self.__normalise_x = normalise_x
        self.reference_curve = None
        self.__curves = {}
        self.__polygons = {}
        self.__maxy = 0
        self.__miny = 0

    def artists(self):
        '''
        Gets the artists painting on this axes.
        :return: the artists.
        '''
        return list(self.__curves.values())

    def curve_names(self):
        '''
        The artist names.
        :return: the names.
        '''
        return list(self.__curves.keys())

    def display_curves(self):
        '''
        Displays the cached data on the specified axes, removing existing curves as required.
        :param data: the data.
        :param curves: the stored curves.
        :param axes: the axes on which to display.
        '''
        if self.__provider is not None:
            data = self.__provider.getMagnitudeData(reference=self.reference_curve)
            if len(data) > 0:
                curve_names = [self.__create_or_update_curve(x) for x in data if data is not None]
                self.__miny = math.floor(min([x.miny for x in data]))
                self.__maxy = math.ceil(max([x.maxy for x in data]))
            else:
                curve_names = []
            self.__delete_old(curve_names, self.__curves)
            self.__delete_old(curve_names, self.__polygons)

    def __delete_old(self, names, artists):
        to_delete = {name: artist for name, artist in artists.items() if name not in names}
        for name, artist in to_delete.items():
            artist.remove()
            del artists[name]

    def __create_or_update_curve(self, data):
        '''
        sets the data on the curve, creating a new artist if necessary.
        :param data: the data to set on the curve.
        :param the updated (or created) curve.
        :return the curve name.
        '''
        curve = self.__curves.get(data.name, None)
        from model.xy import MagnitudeData
        if isinstance(data, MagnitudeData) and self.__normalise_x is True:
            data = data.normalise_x()
        if curve:
            curve.set_data(data.x, data.y)
            curve.set_linestyle(data.linestyle)
            curve.set_color(data.colour)
        else:
            self.__curves[data.name] = self.__axes.semilogx(data.x, data.y,
                                                            linewidth=2,
                                                            antialiased=True,
                                                            linestyle=data.linestyle,
                                                            color=data.colour,
                                                            label=data.name,
                                                            picker=2)[0]
        if self.__fill_curves:
            polygon = self.__polygons.get(data.name, None)
            if polygon:
                polygon.remove()
            self.__polygons[data.name] = self.__axes.fill_between(data.x, data.y,
                                                                  color=data.colour,
                                                                  alpha=self.__fill_alpha)
        return data.name

    def get_ylimits(self):
        '''
        :return: min y, max y
        '''
        return self.__miny, self.__maxy

    def make_legend(self, lines, ncol):
        '''
        makes a legend for the given lines.
        :param lines: the lines to display
        :param ncol: the no of columns to put them in.
        :return the legend.
        '''
        return self.__axes.legend(lines, [l.get_label() for l in lines], loc=3, ncol=ncol, fancybox=True, shadow=True)

    def hide_axes_if_empty(self):
        '''
        Hides the axes if there is nothing here.
        '''
        if self.__axes is not None:
            self.__axes.get_yaxis().set_visible(len(self.curve_names()) > 0)


class MagnitudeModel:
    '''
    Allows a set of filters to be displayed on a chart as magnitude responses.
    '''

    def __init__(self, name, chart, preferences, primary_data_provider, primary_name, secondary_data_provider=None,
                 secondary_name=None, show_legend=lambda: True, db_range_calc=dBRangeCalculator(60),
                 subplot_spec=SINGLE_SUBPLOT_SPEC, redraw_listener=None, grid_alpha=0.5, x_min_pref_key=GRAPH_X_MIN,
                 x_max_pref_key=GRAPH_X_MAX, x_scale_pref_key=GRAPH_X_AXIS_SCALE, fill_curves=False, fill_alpha=0.5,
                 allow_line_resize=False, normalise_x=True):
        self.__name = name
        self.__chart = chart
        self.__redraw_listener = redraw_listener
        self.__show_legend = show_legend
        if allow_line_resize:
            self.__chart.canvas.mpl_connect('pick_event', self.__adjust_line_size)
        primary_axes = self.__chart.canvas.figure.add_subplot(subplot_spec)
        primary_axes.set_ylabel(f"dBFS ({primary_name})")
        primary_axes.grid(linestyle='-', which='major', linewidth=1, alpha=grid_alpha)
        primary_axes.grid(linestyle='--', which='minor', linewidth=1, alpha=grid_alpha * 0.5)
        self.__primary = AxesManager(primary_data_provider, primary_axes, fill_curves, fill_alpha,
                                     normalise_x=normalise_x)
        if secondary_data_provider is None:
            secondary_axes = None
        else:
            secondary_axes = primary_axes.twinx()
            secondary_axes.set_ylabel(f"dBFS ({secondary_name})")
            # bump the z axis so pick events are directed to the primary
            primary_axes.set_zorder(secondary_axes.get_zorder() + 1)
            primary_axes.patch.set_visible(False)
        self.__secondary = AxesManager(secondary_data_provider, secondary_axes, fill_curves, fill_alpha)
        self.limits = Limits(self.__repr__(), self.__redraw_func, primary_axes,
                             x_lim=(preferences.get(x_min_pref_key), preferences.get(x_max_pref_key)),
                             y_range_calculator=db_range_calc, axes_2=secondary_axes,
                             x_scale=preferences.get(x_scale_pref_key))
        self.limits.propagate_to_axes(draw=True)
        self.__legend = None
        self.__legend_cid = None
        self.redraw()

    def __adjust_line_size(self, event):
        ''' Increases or decreases the line size with each click as long as shift is not held down. '''
        from matplotlib.lines import Line2D
        if isinstance(event.artist, Line2D):
            line = event.artist
            if line in self.__primary.artists() or line in self.__secondary.artists():
                if event.mouseevent.button:
                    if event.mouseevent.button == 1:
                        line.set_linewidth(line.get_linewidth() + 1)
                        self.__chart.canvas.draw_idle()
                    elif event.mouseevent.button == 2 or event.mouseevent.button == 3:
                        line.set_linewidth(max(1, line.get_linewidth() - 1))
                        self.__chart.canvas.draw_idle()

    def __redraw_func(self):
        self.__chart.canvas.draw_idle()
        if callable(self.__redraw_listener):
            self.__redraw_listener()

    def __repr__(self):
        return self.__name

    def redraw(self):
        '''
        Gets the current state of the graph
        '''
        self.__display_all_curves()
        self.__make_legend()
        self.__chart.canvas.draw_idle()

    def show_limits(self):
        '''
        Shows the limits dialog.
        '''
        LimitsDialog(self.limits).exec()

    def show_values(self):
        '''
        Shows the values dialog.
        '''
        ValuesDialog(self.__primary.artists() + self.__secondary.artists()).exec()

    def get_curve_names(self, primary=True):
        '''
        :param primary: if true get the primary curves.
        :return: the names of all the curves in the chart.
        '''
        return self.__primary.curve_names() if primary else self.__secondary.curve_names()

    def __display_all_curves(self):
        '''
        Updates all the curves with the currently cached data.
        '''
        self.__primary.display_curves()
        self.__secondary.display_curves()
        self.limits.configure_x_axis()
        self.__secondary.hide_axes_if_empty()
        self.limits.on_data_change(self.__primary.get_ylimits(), self.__secondary.get_ylimits())

    def __make_legend(self):
        '''
        Add a legend that allows you to make a line visible or invisible by clicking on it.
        ripped from https://matplotlib.org/2.0.0/examples/event_handling/legend_picking.html
        and https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
        '''
        if self.__legend is not None:
            self.__legend.remove()
        if self.__legend_cid is not None:
            self.__chart.canvas.mpl_disconnect(self.__legend_cid)

        if self.__show_legend():
            lines = self.__primary.artists() + self.__secondary.artists()
            if len(lines) > 0:
                ncol = int(len(lines) / 3) if len(lines) % 3 == 0 else int(len(lines) / 3) + 1
                self.__legend = self.__primary.make_legend(lines, ncol)
                lined = dict()
                for legline, origline in zip(self.__legend.get_lines(), lines):
                    legline.set_picker(5)  # 5 pts tolerance
                    lined[legline] = origline

                # find the line corresponding to the legend proxy line and toggle the alpha
                def onpick(event):
                    if self.__legend is not None and event.artist in self.__legend.get_lines():
                        legline = event.artist
                        origline = lined[legline]
                        vis = not origline.get_visible()
                        origline.set_visible(vis)
                        legline.set_alpha(1.0 if vis else 0.2)
                        self.__chart.canvas.draw_idle()

                self.__legend_cid = self.__chart.canvas.mpl_connect('pick_event', onpick)

    def normalise(self, primary=True, curve=None):
        '''
        Sets the data series that will act as the reference.
        :param curve: the reference curve (if any).
        '''
        if primary is True:
            self.__primary.reference_curve = curve
        else:
            self.__secondary.reference_curve = curve
        self.redraw()

    def set_visible(self, visible):
        ''' changes chart visibility '''
        self.__chart.setVisible(visible)

    def is_visible(self):
        '''
        :return: true if the chart is visible.
        '''
        return self.__chart.isVisible()
