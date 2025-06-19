from typing import Optional

from pydantic_xml import BaseXmlModel, element, wrapped

from forem_api_client.xml_models.position_opening_elements.contact_method.contact_method import ContactMethod
from forem_api_client.xml_models.position_opening_elements.supplier_id import SupplierId


class Organization(BaseXmlModel, tag='Organization', skip_empty=True):

    organization_name: Optional[str] = element(tag='OrganizationName', default=None)
    legal_id: Optional[SupplierId] = element(tag='LegalId', default=None)
    contact_method: ContactMethod = wrapped('ContactInfo')