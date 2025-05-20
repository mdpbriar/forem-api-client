from pydantic_xml import BaseXmlModel, element

from src.xml_models.contact_method.contact_method import ContactMethod
from src.xml_models.supplier_id import SupplierId


class Organization(BaseXmlModel, tag='Organization', skip_empty=True):

    organization_name: str = element(tag='OrganizationName', default=None)
    legal_id: SupplierId = element(tag='LegalId', default=None)
    contact_method: ContactMethod = element()