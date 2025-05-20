import xml.dom.minidom

from pydantic import BaseModel

from src.xml_models.position_opening import PositionOpening


class ForemXmlBuilder(BaseModel):
    position_opening: PositionOpening
    api_url: str = None
    api_key: str = None


    def build(self) -> bytes:
        # trick pour remplacer lang par xml:lang, à remplacer dans une future version de pydantic-xml
        xml_bytes = self.position_opening.to_xml(encoding='UTF-8')
        xml_str = xml_bytes.decode('UTF-8')
        xml_str = xml_str.replace(' lang="', ' xml:lang="')

        dom = xml.dom.minidom.parseString(xml_str)
        return dom.toxml(encoding='UTF-8')

    def _check_api_credentials(self):
        if not self.api_url:
            raise ValueError('API url must be set')
        if not self.api_key:
            raise ValueError('API key must be set')

    def validate_position_opening(self):
        self._check_api_credentials()


    def send_position_opening(self):
        self._check_api_credentials()
