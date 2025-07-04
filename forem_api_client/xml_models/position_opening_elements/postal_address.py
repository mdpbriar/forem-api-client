from typing import Annotated, Optional

from pydantic import AfterValidator
from pydantic_xml import element, BaseXmlModel

from forem_api_client import validators
from forem_api_client.xml_models.position_opening_elements.delivery_address import DeliveryAddress
from forem_api_client.xml_models.position_opening_elements.recipient import Recipient



class PostalAddress(BaseXmlModel, tag='PostalAddress', skip_empty=True):
    country_code: Annotated[str, AfterValidator(validators.validate_country_code)] = element(tag="CountryCode")
    postal_code: str = element(tag="PostalCode")
    municipality: Optional[str] = element(tag="Municipality", default=None)
    delivery_address: Optional[DeliveryAddress] = element(default=None)
    recipient : Optional[Recipient] = element(default=None)



