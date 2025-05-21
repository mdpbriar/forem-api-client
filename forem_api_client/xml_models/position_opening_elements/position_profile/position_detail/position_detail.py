from typing import Annotated, List, Optional

from pydantic import AfterValidator, field_validator
from pydantic_xml import BaseXmlModel, element, wrapped

from forem_api_client import validators
from forem_api_client.nomenclatures_models.contrattravail import contrat_travail
from forem_api_client.nomenclatures_models.tempstravail import temps_travail
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency import Competency
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.experience import Experience
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.job_category import JobCategory
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.physical_location import PhysicalLocation
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.industry_code import IndustryCode
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.position_schedule import PositionSchedule
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.remuneration_package import RemunerationPackage
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.shift import Shift


class PositionDetail(BaseXmlModel, tag='PositionDetail', skip_empty=True):

    industry_code: IndustryCode = element()
    physical_locations: Annotated[List[PhysicalLocation], AfterValidator(validators.forbid_empty_list)]
    job_categories: List[JobCategory] = element()
    position_title: str = element(tag='PositionTitle')
    contrat_travail: str = element(tag='PositionClassification')
    position_schedules: List[PositionSchedule] = element()
    shifts: Optional[List[Shift]] = element(default=None)
    competencies: List[Competency] = element()
    remuneration_package: Optional[RemunerationPackage] = element(default=None)
    experience: Experience = wrapped('UserArea', element())

    @field_validator('contrat_travail')
    @classmethod
    def validate_contrat_travail(cls, value):
        return validators.validate_nomenclature(value, contrat_travail)


    @field_validator('job_categories')
    @classmethod
    def validate_unique_types(cls, values: List[JobCategory]):
        seen_types = set()
        for job_category in values:
            if job_category.taxonomy_name.value in seen_types:
                raise ValueError("Il ne peut y avoir deux catégories de même type")
            seen_types.add(job_category.taxonomy_name.value)
        return values


    @field_validator('position_schedules')
    @classmethod
    def validate_unique_type_temps(cls, values: List[PositionSchedule]):
        seen_types = set()
        for position_schedule in values:
            type_temps = temps_travail.get_type(position_schedule.value)
            if type_temps in seen_types:
                raise ValueError("Il ne peut y avoir des catégories de temps de travail similaires")
            seen_types.add(type_temps)
        return values


