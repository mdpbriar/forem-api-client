from typing import List, Optional
from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.company_vehicle import CompanyVehicle
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefit import Benefit


class Benefits(BaseXmlModel, tag='Benefits', skip_empty=True):

    insurances: Optional[List[Benefit]] = element(tag='Insurance', default=None)
    company_vehicle: Optional[CompanyVehicle] = element(default=None)
    other_benefits: Optional[List[Benefit]] = element(tag='OtherBenefits', default=None)
