from typing import Optional

from pydantic import EmailStr, HttpUrl
from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.contact_method.telephone import Telephone
from forem_api_client.xml_models.position_opening_elements.postal_address import PostalAddress


class ApplicationMethod(BaseXmlModel, tag='ApplicationMethod', skip_empty=True):

    telephone: Optional[Telephone] = element(tag='Telephone', default=None)
    internet_email_address: Optional[EmailStr] = element(tag='InternetEmailAddress', default=None)
    internet_web_address: Optional[HttpUrl] = element(tag='InternetWebAddress', default=None)
    postal_address: Optional[PostalAddress] = element(default=None)