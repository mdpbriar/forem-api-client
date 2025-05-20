import pandas as pd

from src.nomenclatures_models.base import BaseNomenclature
from src.nomenclatures_models.dimeco import dimeco
from src.nomenclatures_models.romev3 import romev3


class ProvenExperience(BaseNomenclature):

    file = 'dimeco'

    def __init__(self):
        self.data = pd.concat([dimeco.data, romev3.data])


proven_experience = ProvenExperience()