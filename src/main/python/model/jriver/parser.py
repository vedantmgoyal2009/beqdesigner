import json
import logging
from pathlib import Path
from typing import List

from model.iir import ComplexFilter, SOS
from model.jriver.codec import get_peq_key_name, filts_to_xml, include_filters_in_dsp
from model.jriver.common import JRIVER_CHANNELS, get_channel_indexes
from model.jriver.filter import convert_filter_to_mc_dsp, MSOFilter, Filter, Delay, Peak, LowShelf, HighShelf, AllPass

logger = logging.getLogger('jriver.parser')


class JRiverParser:

    def __init__(self, block=0, channels=('Subwoofer',)):
        self.__block = get_peq_key_name(block)
        self.__target_channels = ';'.join([str(JRIVER_CHANNELS.index(c)) for c in channels])

    def convert(self, dst, filt: ComplexFilter, **kwargs):
        from model.minidsp import flatten_filters
        flat_filts: List[SOS] = flatten_filters(filt)
        config_txt = Path(dst).read_text()
        if len(flat_filts) > 0:
            logger.info(f"Copying {len(flat_filts)} to {dst}")
            # generate the xml formatted filters
            xml_filts = [filts_to_xml(convert_filter_to_mc_dsp(f, self.__target_channels).get_all_vals())
                         for f in flat_filts]
            config_txt = include_filters_in_dsp(self.__block, config_txt, xml_filts, replace=False)
        else:
            logger.warning(f"Nop for empty filter file {dst}")
        return config_txt, False

    @staticmethod
    def file_extension():
        return '.dsp'

    @staticmethod
    def newline():
        return '\r\n'


def from_mso(mso: str) -> MSOFilter:
    '''
    :param mso: an exported filter set from MSO.
    :return: the filter set in beqd format.
    '''
    mso_json = json.loads(mso)
    mso_filters = mso_json.get('mso_filters', None)
    if mso_filters:
        return MSOFilter([convert_mso_filter(f) for f in mso_filters])
    else:
        raise ValueError('Unknown mso export format')


def convert_mso_filter(mso_filter: dict) -> Filter:
    f_type = mso_filter['_type']
    channels = ';'.join([str(i) for i in get_channel_indexes(mso_filter['chans'])])
    if f_type == 'Delay':
        return Delay(Delay.default_values() | {'Channels': channels, 'Delay': f"{mso_filter['delay_val']:.12g}"})
    elif f_type == 'PeakingEQ':
        return Peak(Peak.default_values() | {'Channels': channels,
                                             'Gain': f"{mso_filter['gain']:.12g}",
                                             'Frequency': f"{mso_filter['fc']:.12g}",
                                             'Q': f"{mso_filter['q']:.12g}"})
    elif f_type == 'LowShelf':
        return LowShelf(LowShelf.default_values() | {'Channels': channels,
                                                     'Gain': f"{mso_filter['gain']:.12g}",
                                                     'Frequency': f"{mso_filter['fc']:.12g}",
                                                     'Q': f"{mso_filter['q']:.12g}"})
    elif f_type == 'HighShelf':
        return HighShelf(HighShelf.default_values() | {'Channels': channels,
                                                       'Gain': f"{mso_filter['gain']:.12g}",
                                                       'Frequency': f"{mso_filter['fc']:.12g}",
                                                       'Q': f"{mso_filter['q']:.12g}"})
    elif f_type == 'AllPass':
        return AllPass(AllPass.default_values() | {'Channels': channels,
                                                   'Frequency': f"{mso_filter['fc']:.12g}",
                                                   'Q': f"{mso_filter['q']:.12g}"})
    else:
        raise ValueError(f"Unknown MSO filter type {json.dumps(mso_filter)}")
