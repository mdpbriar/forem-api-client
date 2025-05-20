from pydantic_xml import BaseXmlModel, attr


class CompetencyId(BaseXmlModel, tag='CompetencyId', skip_empty=True):

    description: str = attr()
    id: str = attr()
