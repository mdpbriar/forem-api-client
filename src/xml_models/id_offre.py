from pydantic_xml import BaseXmlModel, element, attr


class IdOffre(BaseXmlModel, tag="Id", skip_empty=True):

    id_owner: str = attr(name='idOwner')
    id_value: int|str = element(tag='IdValue')
