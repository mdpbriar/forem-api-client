import pandas as pd

from forem_api_client.nomenclatures_models.base import BaseNomenclature


class RomeV3(BaseNomenclature):

    file = 'romeV3'

    def get_dataframe(self):
        data = self.get_file_content()

        values = pd.DataFrame(data['values'])

        # On filtre pour n'avoir que les id de type A1234
        pattern = r'^[a-zA-Z]\d{4}$'
        return values[values['id'].str.match(pattern, na=False)]



romev3 = RomeV3()