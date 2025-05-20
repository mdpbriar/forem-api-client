from typing import Literal

from pydantic_xml import BaseXmlModel, attr, element


class Shift(BaseXmlModel, tag='Shift', skip_empty=True):

    shift_period: Literal['semaine', 'matin', 'après-midi'] = attr(name='shiftPeriod')
    hours: str = element(tag='Hours', default=None)
    start_time: str = element(tag='StartTime', default=None)
    end_time: str = element(tag='EndTime', default=None)