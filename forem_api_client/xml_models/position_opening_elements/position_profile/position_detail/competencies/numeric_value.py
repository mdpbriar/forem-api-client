from typing import Optional

from pydantic_xml import BaseXmlModel, attr

from forem_api_client.types import CompetencyType


class NumericValue(BaseXmlModel, tag='NumericValue', skip_empty=True):

    minValue: Optional[int] = attr(default=None)
    maxValue: Optional[int] = attr(default=None)
    value: int

    @classmethod
    def make(cls, value: int, competency_type: CompetencyType, min_value:int|None = None, max_value:int|None = None):
        if competency_type == 'Language':
            min_value = 1
            max_value = 6

        if min_value and not value  >= min_value:
            raise ValueError(f"La valeur donnée dans CompetencyEvidence doit être supérieure à sa valeur minimale {min_value}")
        if max_value and not value <= max_value:
            raise ValueError(f"La valeur donnée dans CompetencyEvidence doit être inférieure à sa valeur maximale {max_value}")


        return cls(minValue=min_value, maxValue=max_value, value=value)