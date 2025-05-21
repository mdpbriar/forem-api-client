from typing import Optional

from pydantic_xml import BaseXmlModel, element
from datetime import date

class PositionDateInfo(BaseXmlModel, tag='PositionDateInfo', skip_empty=True):

    start_date: Optional[date] = element(tag='StartDate', default=None)
    expected_end_date: Optional[date] = element(tag='ExpectedEndDate', default=None)
    as_soon_as_possible: Optional[bool] = element(tage='StartAsSoonAsPossible', default=None)
