from pydantic_xml import BaseXmlModel, xml_field_serializer
from pydantic_xml.element import XmlElementWriter

from lxml.etree import CDATA

class EntityName(BaseXmlModel, tag="EntityName", skip_empty=True, arbitrary_types_allowed=True):

    content: str

    @xml_field_serializer('content')
    def serialize_text(self, element: XmlElementWriter, value: str, field_name: str) -> None:
        element.set_text(CDATA(value))
