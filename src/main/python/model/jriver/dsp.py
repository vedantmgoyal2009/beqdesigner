from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as et
from builtins import isinstance
from typing import Dict, Optional, List, Tuple, Type, Callable

from model.jriver.codec import get_peq_block_order, get_output_format, NoFiltersError, get_peq_key_name, \
    extract_filters, filts_to_xml, include_filters_in_dsp, item_to_dicts
from model.jriver.common import OutputFormat, get_channel_name, user_channel_indexes
from model.jriver.filter import FilterGraph, create_peq, Filter, Divider, complex_filter_classes_by_type, set_filter_ids
from model.log import to_millis
from model.signal import Signal

logger = logging.getLogger('jriver.dsp')


class JRiverDSP:

    def __init__(self, name: str, txt_provider: Callable[[], str], colours: Tuple[str, str] = (None,),
                 on_delta: Callable[[bool, bool], None] = None, convert_q: bool = False, allow_padding: bool = False):
        self.__active_idx = 0
        self.__on_delta = on_delta
        self.__filename = name
        self.__colours = colours
        start = time.time()
        self.__input_config_txt = txt_provider()
        peq_block_order = get_peq_block_order(self.__input_config_txt)
        self.__output_format: OutputFormat = get_output_format(self.__input_config_txt, allow_padding)
        self.__graphs: List[FilterGraph] = []
        self.__signals: Dict[str, Signal] = {}
        for block in peq_block_order:
            out_names = self.channel_names(output=True)
            in_names = out_names if self.__graphs else self.channel_names(output=False)
            try:
                mc_filters = self.__parse_peq(self.__input_config_txt, block, convert_q)
            except NoFiltersError:
                mc_filters = []
            self.__graphs.append(FilterGraph(block, in_names, out_names, mc_filters, on_delta))
        end = time.time()
        logger.info(f"Parsed {name} in {to_millis(start, end)}ms")

    @property
    def output_format(self) -> OutputFormat:
        return self.__output_format

    @property
    def filename(self):
        return self.__filename

    @property
    def signals(self) -> List[Signal]:
        return list(self.__signals.values()) if self.__signals else []

    @property
    def graph_count(self) -> int:
        return len(self.__graphs)

    def graph(self, idx) -> FilterGraph:
        return self.__graphs[idx]

    def as_dot(self, idx, vertical=True, selected_nodes=None) -> str:
        return self.graph(idx).render(colours=self.__colours, vertical=vertical, selected_nodes=selected_nodes)

    def channel_names(self, short=True, output=False, exclude_user=False):
        idxs = self.output_format.output_channel_indexes if output else self.output_format.input_channel_indexes
        return [get_channel_name(i, short=short) for i in idxs if not exclude_user or i not in user_channel_indexes()]

    @staticmethod
    def channel_name(i):
        return get_channel_name(i)

    def __parse_peq(self, xml, block, convert_q):
        peq_block = get_peq_key_name(block)
        _, filt_element = extract_filters(xml, peq_block)
        filt_fragments = [v + ')' for v in filt_element.text.split(')') if v]
        if len(filt_fragments) < 2:
            raise ValueError('Invalid input file - Unexpected <Value> format')
        individual_filters = [create_peq(d, convert_q) for d in [item_to_dicts(f) for f in filt_fragments[2:]] if d]
        return self.__extract_custom_filters(individual_filters)

    @staticmethod
    def __extract_custom_filters(individual_filters: List[Filter]) -> List[Filter]:
        '''
        Combines individual filters into ComplexFilter instances based on divider text.
        :param individual_filters: the raw filters.
        :return: the coalesced filters.
        '''
        output_filters: List[Filter] = []
        buffer_stack: List[Tuple[Type, str, List[Filter]]] = []
        for f in individual_filters:
            if isinstance(f, Divider):
                JRiverDSP.__handle_divider(buffer_stack, output_filters, f)
            else:
                store_in = buffer_stack[-1][2] if buffer_stack else output_filters
                store_in.append(f)
        return set_filter_ids(output_filters)

    @staticmethod
    def __handle_divider(buffer: List[Tuple[Type, str, List[Filter]]], output_filters: List[Filter], f: Divider):
        match = next((c.get_complex_filter_data(f.text) for c in complex_filter_classes_by_type.values()
                      if c.get_complex_filter_data(f.text)), None)
        if match is None:
            if buffer:
                buffer[-1][2].append(f)
            else:
                logger.debug(f"Ignoring divider outside complex filter parsing - {f.text}")
        else:
            filt_cls, data = match
            is_end = filt_cls.is_end_of_complex_filter_data(f.text)
            if is_end:
                if buffer:
                    if filt_cls == buffer[-1][0]:
                        _, meta, accumulated = buffer.pop()
                        complex_filt = filt_cls.create(meta, accumulated)
                        store_in = buffer[-1][2] if buffer else output_filters
                        store_in.append(complex_filt)
                    else:
                        raise ValueError(f"Mismatched start/end complex filter detected {buffer[0]} vs {filt_cls}")
                else:
                    raise ValueError(f"Empty complex filter {buffer}")
            else:
                buffer.append((filt_cls, data, []))
        return buffer

    def __repr__(self):
        return f"{self.__filename}"

    def activate(self, active_idx: int) -> None:
        '''
        Activates the selected graph & generates signals accordingly.
        :param active_idx: the active graph index.
        '''
        self.__active_idx = active_idx
        self.active_graph.activate()
        self.simulate()

    def simulate(self):
        self.__signals = self.active_graph.simulate()

    @property
    def active_graph(self) -> FilterGraph:
        return self.graph(self.__active_idx)

    def write_to_file(self, file=None) -> None:
        '''
        Writes the dsp config to the default file or the file provided.
        :param file: the file, if any.
        '''
        output_file = self.filename if file is None else file
        logger.info(f"Writing to {output_file}")
        with open(output_file, mode='w', newline='\r\n') as f:
            f.write(self.config_txt())
        logger.info(f"Written new config to {output_file}")

    def config_txt(self, convert_q: bool = False) -> str:
        new_txt = self.__input_config_txt
        for graph in self.__graphs:
            xml_filts = [filts_to_xml(f.get_all_vals(convert_q=convert_q)) for f in graph.filters]
            new_txt = include_filters_in_dsp(get_peq_key_name(graph.stage), new_txt, xml_filts)
        return new_txt
