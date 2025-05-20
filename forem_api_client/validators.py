from typing import Literal

from src.nomenclatures_models.base import BaseNomenclature
from src.nomenclatures_models.pays import pays
from src.nomenclatures_models.nacebel2008 import nacebel
from src.nomenclatures_models.dimeco import dimeco
from src.nomenclatures_models.romev3 import romev3

def forbid_empty_list(values: list) -> list:
    if len(values) == 0:
        raise ValueError('Cannot be an empty list')
    return values


def validate_digit_string(value: str) -> str:
    if not value.isdigit():
        raise ValueError('The string must contain only digits')
    return value


def validate_country_code(value: str) -> str:
    if not pays.validate_id(value):
        raise ValueError('Invalid country code')
    return value

def validate_nacebel(value: str) -> str:
    if not nacebel.validate_id(value):
        raise ValueError('Invalid nacebel code')
    return value


def validate_taxonomy(value: str, type: Literal['ROMEV3', 'DIMECO']) -> str:
    if type == 'ROMEV3' and not romev3.validate_id(value):
        raise ValueError('Invalid rome V3 code')
    if type == 'DIMECO' and not dimeco.validate_id(value):
        raise ValueError('Invalid dimeco code')
    return value

def validate_nomenclature(value: str, nomenclature: BaseNomenclature) -> str:
    if not nomenclature.validate_id(value):
        raise ValueError(f"Le code {value} n'existe pas dans {nomenclature.file}")
    return value