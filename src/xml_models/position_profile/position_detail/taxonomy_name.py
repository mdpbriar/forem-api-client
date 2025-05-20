from typing import Literal

from pydantic_xml import BaseXmlModel, attr


class TaxonomyName(BaseXmlModel, tag='TaxonomyName', skip_empty=True):

    value: Literal['ROMEV3', 'DIMECO']
    version: str = attr(default='1.0')