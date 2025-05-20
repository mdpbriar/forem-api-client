from typing import Literal, TypeAlias

from src.nomenclatures_models.competence import competence
from src.nomenclatures_models.competencenumerique import competence_numerique
from src.nomenclatures_models.langue import langue
from src.nomenclatures_models.niveauetude import niveau_etude
from src.nomenclatures_models.permisconduire import permis_conduire
from src.nomenclatures_models.provenexperience import proven_experience

CompetencyType: TypeAlias = Literal['Study Code', 'Drivers License', 'Language', 'Competency', 'Proven Experience', 'Office Skills' ]

mapping_competencies = {
    'Study Code': niveau_etude,
    'Drivers License': permis_conduire,
    'Language': langue,
    'Competency': competence,
    'Proven Experience': proven_experience,
    'Office Skills':competence_numerique
}