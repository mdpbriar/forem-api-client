from pydantic_xml import BaseXmlModel, element


class PersonName(BaseXmlModel, tag="PersonName", skip_empty=True):

    preferred_given_name: str = element(tag="PreferredGivenName", default=None)
    family_name: str = element(tag="FamilyName", default=None)
    formatted_name: str = element(tag="FormattedName", default=None)
    affix: str = element(tag="Affix", default=None)