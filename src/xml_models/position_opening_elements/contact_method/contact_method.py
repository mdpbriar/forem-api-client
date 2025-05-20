from pydantic import EmailStr, HttpUrl
from pydantic_xml import BaseXmlModel, element

from src.xml_models.position_opening_elements.contact_method.telephone import Telephone
from src.xml_models.position_opening_elements.postal_address import PostalAddress


class ContactMethod(BaseXmlModel, tag='ContactMethod', skip_empty=True):

    telephone: Telephone = element(tag='Telephone')
    internet_email_address: EmailStr = element(tag='InternetEmailAddress')
    internet_web_address: HttpUrl = element(tag='InternetWebAddress')
    mobile: Telephone = element(tag='Mobile', default=None)
    fax: Telephone = element(tag='Fax', default=None)
    postal_address: PostalAddress = element()