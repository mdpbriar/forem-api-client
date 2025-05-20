from pydantic_xml import BaseXmlModel, attr

class CompanyVehicle(BaseXmlModel, tag='CompanyVehicle', skip_empty=True):

    company_offered: bool = attr(name="companyOffered", default=True)
