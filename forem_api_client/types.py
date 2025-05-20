from typing import Literal, TypeAlias

from forem_api_client.nomenclatures_models.competence import competence
from forem_api_client.nomenclatures_models.competencenumerique import competence_numerique
from forem_api_client.nomenclatures_models.langue import langue
from forem_api_client.nomenclatures_models.niveauetude import niveau_etude
from forem_api_client.nomenclatures_models.permisconduire import permis_conduire
from forem_api_client.nomenclatures_models.provenexperience import proven_experience

CompetencyType: TypeAlias = Literal['Study Code', 'Drivers License', 'Language', 'Competency', 'Proven Experience', 'Office Skills' ]

mapping_competencies = {
    'Study Code': niveau_etude,
    'Drivers License': permis_conduire,
    'Language': langue,
    'Competency': competence,
    'Proven Experience': proven_experience,
    'Office Skills':competence_numerique
}