from pydantic_xml import BaseXmlModel, element

from src.xml_models.position_opening_elements.position_profile.position_detail.base_pay import BasePay
from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefits import Benefits


class RemunerationPackage(BaseXmlModel, tag='RemunerationPackage', skip_empty=True):

    base_pay: BasePay = element(default=None)
    benefits: Benefits = element(default=None)
