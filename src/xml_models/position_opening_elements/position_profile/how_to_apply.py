from pydantic_xml import BaseXmlModel, element, wrapped

from src.xml_models.position_opening_elements.person_name import PersonName
from src.xml_models.position_opening_elements.position_profile.application_method import ApplicationMethod
from src.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue


class HowToApply(BaseXmlModel, tag='HowToApply', skip_empty=True):

    person_name: PersonName = element(tag='PersonName')
    application_method: ApplicationMethod = element()
    comments: CDataValue = wrapped('UserArea', element(tag='Comments', default=None))
    content_posted_information: CDataValue = wrapped('UserArea', element(tag='ContentPostedInformation', default=None))
