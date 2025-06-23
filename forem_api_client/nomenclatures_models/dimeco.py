import pandas as pd

from forem_api_client.nomenclatures_models.base import BaseNomenclature


class Dimeco(BaseNomenclature):

    file = 'dimeco'

    def get_filtered_dataframe(self, romev3_id: str|None = None) -> pd.DataFrame:
        df = self.get_dataframe()
        if romev3_id:
            df = df[df['id'].str.startswith(romev3_id, na=False)]
        return df


    def get_filtered_options(self, romev3_id: str|None = None):
        df = self.get_filtered_dataframe(romev3_id)
        return df.to_dict(orient='records')


dimeco = Dimeco()