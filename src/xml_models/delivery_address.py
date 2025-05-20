from pydantic_xml import BaseXmlModel, element


class DeliveryAddress(BaseXmlModel, tag='DeliveryAddress', skip_empty=True):

    address_line: str = element(tag="AddressLine", default=None)
    street_name: str = element(tag="StreetName", default=None)
    building_number: str = element(tag="BuildingNumber", default=None)
    unit: str = element(tag="Unit", default=None)
    post_office_box: str = element(tag="PostOfficeBox", default=None)
