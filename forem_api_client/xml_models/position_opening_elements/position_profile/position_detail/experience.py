from typing import Literal
from pydantic_xml import BaseXmlModel, attr


class Experience(BaseXmlModel, tag='Experience'):

    unit_of_measure: Literal['Months', 'Years'] = attr(name='unitOfMeasure', default="Years")
    value: int