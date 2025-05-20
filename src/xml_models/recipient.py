from pydantic_xml import BaseXmlModel, element

from src.xml_models.person_name import PersonName


class Recipient(BaseXmlModel, tag="Recipient", skip_empty=True):

    organization_name: str = element(tag="OrganizationName", default=None)
    person_name: PersonName = element(default=None)