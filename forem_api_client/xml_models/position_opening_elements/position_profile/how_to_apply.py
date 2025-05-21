from typing import Optional

from pydantic_xml import BaseXmlModel, element, wrapped

from forem_api_client.xml_models.position_opening_elements.person_name import PersonName
from forem_api_client.xml_models.position_opening_elements.position_profile.application_method import ApplicationMethod
from forem_api_client.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue


class HowToApply(BaseXmlModel, tag='HowToApply', skip_empty=True):

    person_name: PersonName = element(tag='PersonName')
    application_method: ApplicationMethod = element()
    comments: Optional[CDataValue] = wrapped('UserArea', element(tag='Comments', default=None))
    content_posted_information: Optional[CDataValue] = wrapped('UserArea', element(tag='ContentPostedInformation', default=None))
