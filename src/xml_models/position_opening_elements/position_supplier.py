from pydantic_xml import BaseXmlModel, element

from src.xml_models.position_opening_elements.contact_method.contact_method import ContactMethod
from src.xml_models.position_opening_elements.entity_name import EntityName
from src.xml_models.position_opening_elements.supplier_id import SupplierId


class PositionSupplier(BaseXmlModel, tag='PositionSupplier', skip_empty=True):
    id: SupplierId = element()
    entity_name: EntityName = element()
    contact_method: ContactMethod = element()
