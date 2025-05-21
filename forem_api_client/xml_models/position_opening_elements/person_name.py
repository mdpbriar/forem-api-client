from typing import Optional

from pydantic_xml import BaseXmlModel, element


class PersonName(BaseXmlModel, tag="PersonName", skip_empty=True):

    preferred_given_name: Optional[str] = element(tag="PreferredGivenName", default=None)
    family_name: Optional[str] = element(tag="FamilyName", default=None)
    formatted_name: Optional[str] = element(tag="FormattedName", default=None)
    affix: Optional[str] = element(tag="Affix", default=None)