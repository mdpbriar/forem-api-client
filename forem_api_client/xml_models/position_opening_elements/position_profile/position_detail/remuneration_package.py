from typing import Optional

from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.base_pay import BasePay
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefits import Benefits


class RemunerationPackage(BaseXmlModel, tag='RemunerationPackage', skip_empty=True):

    base_pay: Optional[BasePay] = element(default=None)
    benefits: Optional[Benefits] = element(default=None)
