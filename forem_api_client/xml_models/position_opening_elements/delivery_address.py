from typing import Optional

from pydantic_xml import BaseXmlModel, element


class DeliveryAddress(BaseXmlModel, tag='DeliveryAddress', skip_empty=True):

    address_line: Optional[str] = element(tag="AddressLine", default=None)
    street_name: Optional[str] = element(tag="StreetName", default=None)
    building_number: Optional[str] = element(tag="BuildingNumber", default=None)
    unit: Optional[str] = element(tag="Unit", default=None)
    post_office_box: Optional[str] = element(tag="PostOfficeBox", default=None)
