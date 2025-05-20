from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.person_name import PersonName


class Recipient(BaseXmlModel, tag="Recipient", skip_empty=True):

    organization_name: str = element(tag="OrganizationName", default=None)
    person_name: PersonName = element(default=None)