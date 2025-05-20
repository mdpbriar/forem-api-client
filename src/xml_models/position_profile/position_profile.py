from typing import List

from pydantic_xml import BaseXmlModel, attr, element

from src.xml_models.position_profile.organization import Organization
from src.xml_models.position_profile.position_date_info import PositionDateInfo
from src.xml_models.position_profile.position_detail.job_category import JobCategory
from src.xml_models.position_profile.position_detail.position_detail import PositionDetail


class PositionProfile(BaseXmlModel, tag='PositionProfile', skip_empty=True):

    lang: str = attr(name="lang", default='FR')
    position_date_info: PositionDateInfo = element()
    organization: Organization = element()
    position_detail: PositionDetail = element()
