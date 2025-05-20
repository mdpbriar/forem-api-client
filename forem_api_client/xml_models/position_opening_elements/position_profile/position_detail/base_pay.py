from typing import Literal

from pydantic_xml import BaseXmlModel, attr, element

class BasePay(BaseXmlModel, tag='BasePay', skip_empty=True):

    interval: Literal['Weekly', 'Monthly', 'Daily', 'Hourly'] = attr(name="baseInterval", default="Monthly")
    currency_code: str = attr(name="currencyCode", default="EUR")
    amount_min: float = element(tag="BasePayAmountMin")
    amount_max: float = element(tag="BasePayAmountMax")
