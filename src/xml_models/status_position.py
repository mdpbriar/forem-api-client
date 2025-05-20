from datetime import date
from typing import Literal

from pydantic_xml import BaseXmlModel, element, attr


class StatutPosition(BaseXmlModel, tag="Status", skip_empty=True):

    valid_from: date = attr(name="validFrom")
    valid_to: date = attr(name="validTo")
    content: Literal['Active', 'Inactive', 'Pending']
