import json
import os
import pathlib
from typing import Dict, Literal

import pandas as pd
from pandas import json_normalize


class BaseNomenclature:

    file: str = 'pays'
    data: pd.DataFrame = None
    taxonomy: Dict[Literal['id', 'description'], str] = {}

    def __init__(self):
        self.data = self.get_dataframe()
        self.taxonomy = self.get_taxonomy()

    def get_taxonomy(self):
        data = self.get_file_content()
        return data.get('taxonomy', {})


    def get_file_content(self):
        path = os.path.join(
            pathlib.Path(__file__).parent.parent.resolve(),
            'nomenclatures',
            self.file
        )
        with open(path) as file:
            return json.load(file)


    def get_version(self):
        data = self.get_file_content()
        return data['version']


    def get_dataframe(self):
        data = self.get_file_content()

        return pd.DataFrame(data['values'])


    def validate_id(self, value: str):
        df = self.data
        return value in df['id'].values

    def get_description_for_id(self, value:str):
        try:
            return self.data.loc[self.data['id'] == value]['description'].values[0]
        except IndexError:
            raise ValueError(f"Le code {value} n'a pas été trouvé dans {self.file}")


