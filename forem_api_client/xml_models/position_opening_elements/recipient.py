from typing import Optional

from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.person_name import PersonName


class Recipient(BaseXmlModel, tag="Recipient", skip_empty=True):

    organization_name: Optional[str] = element(tag="OrganizationName", default=None)
    person_name: Optional[PersonName] = element(default=None)