from typing import Literal, Annotated

from pydantic import AfterValidator
from pydantic_xml import BaseXmlModel, attr

from forem_api_client import validators


class IndustryCode(BaseXmlModel, tag='IndustryCode', skip_empty=True):

    classification_name: Literal['NaceBel2008'] = attr(name='classificationName', default="NaceBel2008")
    value: Annotated[str, AfterValidator(validators.validate_nacebel)]