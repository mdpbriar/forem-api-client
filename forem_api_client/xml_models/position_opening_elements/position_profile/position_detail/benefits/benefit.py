from pydantic_xml import BaseXmlModel, attr

class Benefit(BaseXmlModel, tag='Insurance', skip_empty=True):

    type: str = attr()
    value: bool = True