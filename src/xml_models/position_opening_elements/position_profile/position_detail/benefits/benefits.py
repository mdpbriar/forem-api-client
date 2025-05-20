from typing import List
from pydantic_xml import BaseXmlModel, element

from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.company_vehicle import CompanyVehicle
from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefit import Benefit


class Benefits(BaseXmlModel, tag='Benefits', skip_empty=True):

    insurances: List[Benefit] = element(tag='Insurance', default=None)
    company_vehicle: CompanyVehicle = element(default=None)
    other_benefits: List[Benefit] = element(tag='OtherBenefits', default=None)
