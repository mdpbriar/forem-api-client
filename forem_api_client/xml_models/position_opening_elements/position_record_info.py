from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.id_offre import IdOffre
from forem_api_client.xml_models.position_opening_elements.status_position import StatutPosition


class PositionRecordInfo(BaseXmlModel, tag="PositionRecordInfo", skip_empty=True):
    id: IdOffre = element()
    status: StatutPosition = element()



