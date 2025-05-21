from typing import Annotated, Optional

from pydantic import AfterValidator
from pydantic_xml import BaseXmlModel, element
from forem_api_client import validators


class Telephone(BaseXmlModel, tag="Telephone", skip_empty=True):

    formatted_number: Optional[str] = element(tag='FormattedNumber', default=None)
    international_country_code: Optional[Annotated[str, AfterValidator(validators.validate_digit_string)]] = element(tag='InternationalCountryCode', default=None)
    area_city_code: Optional[Annotated[str, AfterValidator(validators.validate_digit_string)]] = element(tag='AreaCityCode', default=None)
    subscriber_number: Annotated[str, AfterValidator(validators.validate_digit_string)] = element(tag='SubscriberNumber')
