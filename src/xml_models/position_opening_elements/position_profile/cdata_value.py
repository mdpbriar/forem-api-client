from typing import Literal

from pydantic_xml import BaseXmlModel, element, xml_field_serializer
from pydantic_xml.element import XmlElementWriter
from lxml.etree import CDATA


class CDataValue(BaseXmlModel, tag='Value', skip_empty=True):

    value: str

    @xml_field_serializer('value')
    def serialize_text(self, element: XmlElementWriter, value: str, field_name: str) -> None:
        element.set_text(CDATA(value))
