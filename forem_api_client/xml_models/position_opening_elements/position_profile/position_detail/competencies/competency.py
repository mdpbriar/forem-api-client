from typing import Optional

from pydantic import field_validator
from pydantic_xml import BaseXmlModel, attr, element

from forem_api_client.types import CompetencyType, mapping_competencies
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency_id import CompetencyId


class Competency(BaseXmlModel, tag='Competency', skip_empty=True):

    name: CompetencyType = attr(name='name')
    competency_id: CompetencyId = element(tag='CompetencyId')
    taxonomy_id: CompetencyId = element(tag='TaxonomyId')
    competency_evidence: Optional[int] = element(tag='CompetencyEvidence', default=None)

    @field_validator('competency_evidence')
    @classmethod
    def validate_competency_evidence(cls, value, values):
        if value is None and values.data.get('name', None) in ['Language', 'Proven Experience']:
            raise ValueError(f"Une valeur pour Competency Evidence est requise pour une compétence de type {values.data.get('name')}")
        if values.data.get('name') == 'Language' and value not in range(1,6):
            raise ValueError(f"Pour une compétence de type Language, la valeur de CompetencyEvidence doit être comprise entre 1 et 6")
        return value

    @classmethod
    def make(cls, competency_type: CompetencyType, competency_id: int|str, competency_evidence: Optional[int] = None):

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
            competency_evidence=competency_evidence,
        )



