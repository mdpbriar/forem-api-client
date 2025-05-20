from typing import List

from pydantic_xml import BaseXmlModel, attr, element, wrapped

from forem_api_client.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue
from forem_api_client.xml_models.position_opening_elements.position_profile.formatted_position_description import FormattedPositionDescription
from forem_api_client.xml_models.position_opening_elements.position_profile.how_to_apply import HowToApply
from forem_api_client.xml_models.position_opening_elements.position_profile.organization import Organization
from forem_api_client.xml_models.position_opening_elements.position_profile.position_date_info import PositionDateInfo
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.position_detail import PositionDetail


class PositionProfile(BaseXmlModel, tag='PositionProfile', skip_empty=True):

    lang: str = attr(name="lang", default='FR')
    position_date_info: PositionDateInfo = element()
    organization: Organization = element()
    position_detail: PositionDetail = element()
    formatted_descriptions: List[FormattedPositionDescription] = element()
    how_to_apply: HowToApply = element()
    comments: CDataValue = wrapped('UserArea', element(tag='Comments', default=None))
    selection_procedure: CDataValue = wrapped('UserArea', element(tag='SelectionProcedure', default=None))

