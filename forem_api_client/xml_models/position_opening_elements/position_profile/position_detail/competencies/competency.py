from typing import Optional

from pydantic import field_validator
from pydantic_xml import BaseXmlModel, attr, element, wrapped

from forem_api_client.types import CompetencyType, mapping_competencies
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency_id import CompetencyId
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.numeric_value import \
    NumericValue


class Competency(BaseXmlModel, tag='Competency', skip_empty=True):

    name: CompetencyType = attr(name='name')
    competency_id: CompetencyId = element(tag='CompetencyId')
    taxonomy_id: CompetencyId = element(tag='TaxonomyId')
    competency_evidence: Optional[NumericValue] = wrapped('CompetencyEvidence', default=None)

    @field_validator('competency_evidence')
    @classmethod
    def validate_competency_evidence(cls, value, values):
        if value is None and values.data.get('name', None) in ['Language', 'Proven Experience']:
            raise ValueError(f"Une valeur pour Competency Evidence est requise pour une compétence de type {values.data.get('name')}")
        return value

    @classmethod
    def make(cls, competency_type: CompetencyType, competency_id: int|str, competency_evidence: Optional[NumericValue] = None):

        # On récupère le type de nomenclature correspondante
        nomenclature = mapping_competencies.get(competency_type)
        competency_description = nomenclature.get_description_for_id(competency_id)

        return cls(
            name=competency_type,
            competency_id=CompetencyId(
                id=competency_id,
                description=competency_description,
            ),
            taxonomy_id=CompetencyId(
                id=nomenclature.taxonomy.get('id'),
                description=nomenclature.taxonomy.get('description'),
            ),
            competency_evidence=NumericValue.make(
                value=competency_evidence.value,
                competency_type=competency_type,
                min_value=competency_evidence.minValue,
                max_value=competency_evidence.maxValue,
            ) if competency_evidence is not None else None,
        )



