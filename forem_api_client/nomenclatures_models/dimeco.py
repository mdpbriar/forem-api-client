from forem_api_client.nomenclatures_models.base import BaseNomenclature


class Dimeco(BaseNomenclature):

    file = 'dimeco'

    def get_filtered_dataframe(self, romev3_id: str):
        df = self.get_dataframe()
        return df[df['id'].str.startswith(romev3_id, na=False)]

    def get_filtered_options(self, romev3_id: str):
        df = self.get_filtered_dataframe(romev3_id)
        return df.to_dict(orient='records')


dimeco = Dimeco()