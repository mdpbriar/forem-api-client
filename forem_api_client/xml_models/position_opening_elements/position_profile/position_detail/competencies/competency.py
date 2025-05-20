from pydantic_xml import BaseXmlModel, attr, element

from src.types import CompetencyType, mapping_competencies
from src.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency_id import CompetencyId


class Competency(BaseXmlModel, tag='Competency', skip_empty=True):

    name: CompetencyType = attr(name='name')
    competency_id: CompetencyId = element(tag='CompetencyId')
    taxonomy_id: CompetencyId = element(tag='TaxonomyId')


    @classmethod
    def make(cls, competency_type: CompetencyType, competency_id: int|str):

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
        )



