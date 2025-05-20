from typing import Any, Union

from pydantic_xml import BaseXmlModel, element, attr

from src.xml_models.entity_name import EntityName
from src.xml_models.position_profile.position_profile import PositionProfile
from src.xml_models.position_record_info import PositionRecordInfo
from src.xml_models.position_supplier import PositionSupplier

NSMAP = {"": "http://ns.hr-xml.org/2006-02-28", "xsi": "http://www.w3.org/2001/XMLSchema-instance"}

class PositionOpening(BaseXmlModel, tag="PositionOpening", skip_empty=True, nsmap=NSMAP):

    # xsi: str = attr(default='http://www.w3.org/2001/XMLSchema-instance')
    lang: str = attr(name='lang', default='FR')

    position_record_info: PositionRecordInfo = element()
    position_supplier: PositionSupplier = element()
    position_profile: PositionProfile = element()

