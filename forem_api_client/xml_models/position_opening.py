from pydantic_xml import BaseXmlModel, element, attr, wrapped

from forem_api_client.xml_models.position_opening_elements.position_profile.position_profile import PositionProfile
from forem_api_client.xml_models.position_opening_elements.position_record_info import PositionRecordInfo
from forem_api_client.xml_models.position_opening_elements.position_supplier import PositionSupplier

NSMAP = {"": "http://ns.hr-xml.org/2006-02-28", "xsi": "http://www.w3.org/2001/XMLSchema-instance"}

class PositionOpening(BaseXmlModel, tag="PositionOpening", skip_empty=True, nsmap=NSMAP):

    # xsi: str = attr(default='http://www.w3.org/2001/XMLSchema-instance')
    lang: str = attr(name='lang', default='FR')

    position_record_info: PositionRecordInfo = element()
    position_supplier: PositionSupplier = element()
    position_profile: PositionProfile = element()
    number_to_fill: int = element(tag='NumberToFill', default=None)
    total_number_of_jobs: int = wrapped('UserArea', element(tag='TotalNumberOfJobs', default=None))

