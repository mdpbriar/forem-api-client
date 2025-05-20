from pydantic_xml import BaseXmlModel, element

from forem_api_client.xml_models.position_opening_elements.postal_address import PostalAddress


class PhysicalLocation(BaseXmlModel, tag="PhysicalLocation", skip_empty=True):

    postal_address: PostalAddress = element()