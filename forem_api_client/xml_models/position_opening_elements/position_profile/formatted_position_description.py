from typing import Literal

from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue


class FormattedPositionDescription(BaseXmlModel, tag='FormattedPositionDescription', skip_empty=True, arbitrary_types_allowed=True):

    name: Literal['jobDescription', 'contractInformation', 'companyPromotionalText'] = element(tag='Name')
    value: CDataValue = element(tag='Value')