from typing import Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element


class Shift(BaseXmlModel, tag='Shift', skip_empty=True):

    shift_period: Literal['semaine', 'matin', 'après-midi'] = attr(name='shiftPeriod')
    hours: Optional[str] = element(tag='Hours', default=None)
    start_time: Optional[str] = element(tag='StartTime', default=None)
    end_time: Optional[str] = element(tag='EndTime', default=None)