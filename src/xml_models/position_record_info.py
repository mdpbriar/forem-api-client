from pydantic_xml import BaseXmlModel, element

from src.xml_models.id_offre import IdOffre
from src.xml_models.status_position import StatutPosition


class PositionRecordInfo(BaseXmlModel, tag="PositionRecordInfo", skip_empty=True):
    id: IdOffre = element()
    status: StatutPosition = element()



