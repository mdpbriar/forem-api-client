import xml.dom.minidom
from typing import Optional
import httpx
import xmltodict
from httpx import URL, HTTPError

from forem_api_client.xml_models.position_opening import PositionOpening
from forem_api_client.types import ForemDataset


class ForemXmlBuilder:
    position_opening: PositionOpening
    api_url: URL = None
    api_key: str = None
    client: httpx.AsyncClient

    def __init__(self, position_opening: PositionOpening = None, api_url: str = None, api_key: Optional[str] = None):

        if position_opening:
            self.position_opening = position_opening
        if api_url:
            self.api_url = URL(api_url)
        self.api_key = api_key
        if self.api_url:
            self.client = httpx.AsyncClient(base_url=self.api_url,
                                            headers={
                                                'Content-Type': 'text/xml; charset=UTF8',
                                                'Ocp-Apim-Subscription-Key': self.api_key,
                                            })


    def build_xml(self) -> str:
        if not self.position_opening:
            raise AttributeError("PositionOpening must be set before building XML")
        # trick pour remplacer lang par xml:lang, à remplacer dans une future version de pydantic-xml
        xml_bytes = self.position_opening.to_xml(encoding='UTF-8', xml_declaration=True)
        xml_str = xml_bytes.decode('UTF-8')
        xml_str = xml_str.replace(' lang="', ' xml:lang="')

        return xml_str


    def xml_pretty_print(self):
        dom = xml.dom.minidom.parseString(self.build_xml())
        return dom.toxml(encoding='UTF-8')


    def _check_api_credentials(self):
        if not self.api_url:
            raise ValueError('API url must be set')
        if not self.api_key:
            raise ValueError('API key must be set')

    async def validate_position_opening(self):
        self._check_api_credentials()
        r = await self.client.post('/OffresEmploi/Validation', content=self.build_xml() )
        r.raise_for_status()

        response = xmltodict.parse(r.content)
        if (validation_result := response.get('PositionOpeningValidationResult', None)) is None:
            raise HTTPError("Pas de résultat de validation renvoyé par l'API")

        if errors := validation_result.get('Errors', None):
            raise HTTPError(errors)

        return validation_result


    async def send_position_opening(self):
        self._check_api_credentials()
        r = await self.client.post('/OffresEmploi', content=self.build_xml() )
        r.raise_for_status()

        return r.content


    async def get_dataset(self, dataset: ForemDataset, version: str = '1.0'):
        self._check_api_credentials()
        r = await self.client.get(f"/OffresEmploi/OpenData/{version}/{dataset}")
        r.raise_for_status()

        return r.content
