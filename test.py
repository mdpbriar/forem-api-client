from datetime import date, datetime

from forem_api_client.nomenclatures_models.base import BaseNomenclature
from forem_api_client.xml_builder import ForemXmlBuilder
from forem_api_client.xml_models.position_opening_elements.contact_method.contact_method import ContactMethod
from forem_api_client.xml_models.position_opening_elements.contact_method.telephone import Telephone
from forem_api_client.xml_models.position_opening_elements.entity_name import EntityName
from forem_api_client.xml_models.position_opening_elements.id_offre import IdOffre
from forem_api_client.xml_models.position_opening_elements.person_name import PersonName
from forem_api_client.xml_models.position_opening_elements.position_profile.application_method import ApplicationMethod
from forem_api_client.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue
from forem_api_client.xml_models.position_opening_elements.position_profile.formatted_position_description import FormattedPositionDescription
from forem_api_client.xml_models.position_opening_elements.position_profile.how_to_apply import HowToApply
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.base_pay import BasePay
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefits import Benefits
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.company_vehicle import CompanyVehicle
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefit import Benefit
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency import Competency
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.competencies.numeric_value import \
    NumericValue
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.experience import Experience
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.job_category import JobCategory
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.physical_location import PhysicalLocation
from forem_api_client.xml_models.position_opening import PositionOpening
from forem_api_client.xml_models.position_opening_elements.position_profile.organization import Organization
from forem_api_client.xml_models.position_opening_elements.position_profile.position_date_info import PositionDateInfo
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.industry_code import IndustryCode
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.position_detail import PositionDetail
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.position_schedule import PositionSchedule
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.remuneration_package import RemunerationPackage
from forem_api_client.xml_models.position_opening_elements.position_profile.position_detail.shift import Shift
from forem_api_client.xml_models.position_opening_elements.position_profile.position_profile import PositionProfile
from forem_api_client.xml_models.position_opening_elements.position_record_info import PositionRecordInfo
from forem_api_client.xml_models.position_opening_elements.position_supplier import PositionSupplier
from forem_api_client.xml_models.position_opening_elements.postal_address import PostalAddress
from forem_api_client.xml_models.position_opening_elements.recipient import Recipient
import xml.dom.minidom

from forem_api_client.xml_models.position_opening_elements.status_position import StatutPosition
from forem_api_client.xml_models.position_opening_elements.supplier_id import SupplierId


def main():

    recipient = Recipient(
        organization_name="Test",
        person_name=PersonName(family_name="Test")
    )

    postal_address = PostalAddress(country_code='BE', postal_code='12345', recipient=recipient)

    physical_location = PhysicalLocation(postal_address=postal_address)

    # position_detail = PositionDetail(physical_locations=[physical_location, PhysicalLocation(postal_address=PostalAddress(country_code='FR', postal_code='43233'))])

    contact_henallux = ContactMethod(
        telephone=Telephone(
            subscriber_number='746846'
        ),
        internet_email_address='test@test.be',
        internet_web_address='https://test.be',
        postal_address=postal_address,
    )

    position_opening = PositionOpening(
        position_record_info=PositionRecordInfo(
            id=IdOffre(id_owner='test', id_value=5),
            status=StatutPosition(
                valid_to=datetime.strptime('2026-02-01', "%Y-%m-%d"),
                valid_from=date.today(),
                content="Active"
            )
        ),
        position_supplier=PositionSupplier(
            id=SupplierId(value='test'),
            entity_name=EntityName(content="Salut"),
            contact_method=ContactMethod(
                telephone=Telephone(
                    subscriber_number='746846'
                ),
                internet_email_address='test@test.be',
                internet_web_address='https://test.be',
                postal_address=postal_address,
            )
        ),
        position_profile=PositionProfile(
            lang='FR',
            position_date_info=PositionDateInfo(
                start_date=date.today(),
                as_soon_as_possible=False,
            ),
            organization=Organization(
                organization_name="Test",
                contact_method=contact_henallux
            ),
            position_detail=PositionDetail(
                industry_code=IndustryCode(value='0111002'),
                physical_locations=[physical_location],
                job_categories=[
                    JobCategory.make(taxonomy_type='ROMEV3', category_code='A1101'),
                    JobCategory.make(taxonomy_type='DIMECO', category_code='N410301-4'),
                ],
                position_title="Aide internationale",
                contrat_travail='G',
                position_schedules=[
                    PositionSchedule(value='Full Time'),
                    PositionSchedule(value='x:Day Work'),
                ],
                shifts=[
                    Shift(shift_period='matin', hours='4', start_time='8:00', end_time='12:00'),
                ],
                competencies=[
                    Competency.make(
                        competency_type='Drivers License',
                        competency_id='AM',
                        competency_evidence=NumericValue(
                            value=5,
                            minValue=2,
                        )),
                ],
                remuneration_package=RemunerationPackage(
                    base_pay=BasePay(amount_min=1200, amount_max=1800),
                    benefits=Benefits(
                        company_vehicle=CompanyVehicle(),
                        insurances=[Benefit(type='Hospitalisations')],
                        other_benefits=[Benefit(type='Test')]
                    )
                ),
                experience=Experience(value=6)
            ),
            formatted_descriptions=[FormattedPositionDescription(name='companyPromotionalText', value=CDataValue(value='Test'))],
            how_to_apply=HowToApply(
                person_name=PersonName(family_name='Test'),
                application_method=ApplicationMethod(
                    internet_email_address='test@test.be'
                ),
                comments=CDataValue(value="Test"),
                content_posted_information=CDataValue(value="Test"),

            )
        ),
        number_to_fill=4,
        total_number_of_jobs=6
    )

    xml = ForemXmlBuilder(position_opening=position_opening).build_xml()
    print(xml)




if __name__ == '__main__':
    main()