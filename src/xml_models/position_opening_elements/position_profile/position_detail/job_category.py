from typing import Literal

from pydantic import field_validator
from pydantic_xml import BaseXmlModel, element

from src import validators
from src.nomenclatures_models.dimeco import dimeco
from src.nomenclatures_models.romev3 import romev3
from src.xml_models.position_opening_elements.position_profile.position_detail.taxonomy_name import TaxonomyName


class JobCategory(BaseXmlModel, tag='JobCategory', skip_empty=True):

    taxonomy_name: TaxonomyName = element()
    category_code: str = element(tag='CategoryCode')
    category_description: str = element(tag='CategoryDescription')

    @field_validator('category_code')
    @classmethod
    def validate_category_code(cls, v, values):
        return validators.validate_taxonomy(v, values.data['taxonomy_name'])

    @classmethod
    def make(cls, taxonomy_type: Literal['ROMEV3', 'DIMECO'], category_code: str):

        if taxonomy_type == 'ROMEV3':
            nomenclatures = romev3
        if taxonomy_type == 'DIMECO':
            nomenclatures = dimeco

        return cls(
            taxonomy_name=TaxonomyName(value=taxonomy_type),
            category_code=category_code,
            category_description=nomenclatures.get_description_for_id(category_code),
        )


#
#
# class JobCategory(BaseXmlModel, tag='JobCategory', skip_empty=True):
#
#     taxonomy_type: Literal['ROMEV3', 'DIMECO'] = element(tag='TaxonomyName')
#     category_code: str = element(tag='CategoryCode')
#     category_description: str = element(tag='CategoryDescription', default=None)
#
#     @field_validator('category_code')
#     @classmethod
#     def validate_category_code(cls, v, values):
#         return validators.validate_taxonomy(v, values.data['taxonomy_type'])
#
#     @xml_field_serializer('taxonomy_type')
#     def add_attribute(self, element: XmlElementWriter, value: str, field_name: str) -> None:
#         element.set_attribute(name='version', value='1.0')
#
#     @xml_field_serializer('category_description')
#     def serialize_text(self, element: XmlElementWriter, value: str, field_name: str) -> str:
#         pass
# #
# #
# # def to_xml(self, **kwargs: Any) -> Union[str, bytes]:
# #         xml = super().to_xml(**kwargs)
# #         return xml
#
#
