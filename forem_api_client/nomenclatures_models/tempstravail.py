from typing import Literal

from src.nomenclatures_models.base import BaseNomenclature


class TempsTravail(BaseNomenclature):

    file = 'tempstravail'


    @staticmethod
    def get_type(value: str) -> Literal['part_full', 'time_shift']:
        if value.startswith('x:'):
            return 'time_shift'
        return 'part_full'


temps_travail = TempsTravail()