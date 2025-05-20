from typing import Annotated

from pydantic import AfterValidator
from pydantic_xml import element, BaseXmlModel

from src import validators
from src.xml_models.position_opening_elements.delivery_address import DeliveryAddress
from src.xml_models.position_opening_elements.recipient import Recipient



class PostalAddress(BaseXmlModel, tag='PostalAddress', skip_empty=True):
    postal_code: str = element(tag="PostalCode")
    country_code: Annotated[str, AfterValidator(validators.validate_country_code)] = element(tag="CountryCode")
    municipality: str = element(tag="Municipality", default=None)
    delivery_address: DeliveryAddress = element(default=None)
    recipient : Recipient = element(default=None)



