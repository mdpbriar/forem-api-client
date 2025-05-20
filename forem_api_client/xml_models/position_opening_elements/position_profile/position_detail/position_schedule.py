from pydantic import field_validator
from pydantic_xml import BaseXmlModel

from forem_api_client import validators
from forem_api_client.nomenclatures_models.tempstravail import temps_travail


class PositionSchedule(BaseXmlModel, tag='PositionSchedule', skip_empty=True):

    value: str

    @field_validator('value')
    @classmethod
    def validate_temps_travail(cls, value):
        return validators.validate_nomenclature(value, temps_travail)