from datetime import date, datetime

from src.nomenclatures_models.base import BaseNomenclature
from src.xml_models.position_opening_elements.contact_method.contact_method import ContactMethod
from src.xml_models.position_opening_elements.contact_method.telephone import Telephone
from src.xml_models.position_opening_elements.entity_name import EntityName
from src.xml_models.position_opening_elements.id_offre import IdOffre
from src.xml_models.position_opening_elements.person_name import PersonName
from src.xml_models.position_opening_elements.position_profile.application_method import ApplicationMethod
from src.xml_models.position_opening_elements.position_profile.cdata_value import CDataValue
from src.xml_models.position_opening_elements.position_profile.formatted_position_description import FormattedPositionDescription
from src.xml_models.position_opening_elements.position_profile.how_to_apply import HowToApply
from src.xml_models.position_opening_elements.position_profile.position_detail.base_pay import BasePay
from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefits import Benefits
from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.company_vehicle import CompanyVehicle
from src.xml_models.position_opening_elements.position_profile.position_detail.benefits.benefit import Benefit
from src.xml_models.position_opening_elements.position_profile.position_detail.competencies.competency import Competency
from src.xml_models.position_opening_elements.position_profile.position_detail.experience import Experience
from src.xml_models.position_opening_elements.position_profile.position_detail.job_category import JobCategory
from src.xml_models.position_opening_elements.position_profile.position_detail.physical_location import PhysicalLocation
from src.xml_models.position_opening import PositionOpening
from src.xml_models.position_opening_elements.position_profile.organization import Organization
from src.xml_models.position_opening_elements.position_profile.position_date_info import PositionDateInfo
from src.xml_models.position_opening_elements.position_profile.position_detail.industry_code import IndustryCode
from src.xml_models.position_opening_elements.position_profile.position_detail.position_detail import PositionDetail
from src.xml_models.position_opening_elements.position_profile.position_detail.position_schedule import PositionSchedule
from src.xml_models.position_opening_elements.position_profile.position_detail.remuneration_package import RemunerationPackage
from src.xml_models.position_opening_elements.position_profile.position_detail.shift import Shift
from src.xml_models.position_opening_elements.position_profile.position_profile import PositionProfile
from src.xml_models.position_opening_elements.position_record_info import PositionRecordInfo
from src.xml_models.position_opening_elements.position_supplier import PositionSupplier
from src.xml_models.position_opening_elements.postal_address import PostalAddress
from src.xml_models.position_opening_elements.recipient import Recipient
import xml.dom.minidom

from src.xml_models.position_opening_elements.status_position import StatutPosition
from src.xml_models.position_opening_elements.supplier_id import SupplierId


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
                    Competency.make(competency_type='Language', competency_id='fr'),
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

    xml_bytes = position_opening.to_xml(encoding='UTF-8')

    xml_str = xml_bytes.decode('UTF-8')
    xml_str = xml_str.replace(' lang="', ' xml:lang="')


    dom = xml.dom.minidom.parseString(xml_str)
    print(dom.toprettyxml())

    nomenclature = BaseNomenclature()

    print(nomenclature.get_version())


if __name__ == '__main__':
    main()