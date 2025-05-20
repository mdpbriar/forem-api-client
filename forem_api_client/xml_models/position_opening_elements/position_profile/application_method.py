from pydantic import EmailStr, HttpUrl
from pydantic_xml import BaseXmlModel, element

from src.xml_models.position_opening_elements.contact_method.telephone import Telephone
from src.xml_models.position_opening_elements.postal_address import PostalAddress


class ApplicationMethod(BaseXmlModel, tag='ApplicationMethod', skip_empty=True):

    telephone: Telephone = element(tag='Telephone', default=None)
    internet_email_address: EmailStr = element(tag='InternetEmailAddress', default=None)
    internet_web_address: HttpUrl = element(tag='InternetWebAddress', default=None)
    postal_address: PostalAddress = element(default=None)