import xml.dom.minidom

from pydantic import BaseModel

from src.xml_models.position_opening import PositionOpening


class ForemXmlBuilder(BaseModel):
    position_opening: PositionOpening


    def build(self) -> bytes:
        # trick pour remplacer lang par xml:lang, à remplacer dans une future version de pydantic-xml
        xml_bytes = self.position_opening.to_xml(encoding='UTF-8')
        xml_str = xml_bytes.decode('UTF-8')
        xml_str = xml_str.replace(' lang="', ' xml:lang="')

        dom = xml.dom.minidom.parseString(xml_str)
        return dom.toxml(encoding='UTF-8')