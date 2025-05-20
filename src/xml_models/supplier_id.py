from typing import Literal

from pydantic_xml import BaseXmlModel, attr, element


class SupplierId(BaseXmlModel, tag='SupplierId', skip_empty=True):

    id_owner: Literal['BCE', 'KBO', 'PartnerCode'] = attr(name='idOwner', default='PartnerCode')
    value: str = element(tag='IdValue')