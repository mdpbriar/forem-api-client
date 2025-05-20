from datetime import date, datetime

from src.nomenclatures_models.base import BaseNomenclature
from src.xml_models.contact_method.contact_method import ContactMethod
from src.xml_models.contact_method.telephone import Telephone
from src.xml_models.entity_name import EntityName
from src.xml_models.id_offre import IdOffre
from src.xml_models.person_name import PersonName
from src.xml_models.position_profile.position_detail.competencies.competency import Competency
from src.xml_models.position_profile.position_detail.job_category import JobCategory
from src.xml_models.position_profile.position_detail.physical_location import PhysicalLocation
from src.xml_models.position_opening import PositionOpening
from src.xml_models.position_profile.organization import Organization
from src.xml_models.position_profile.position_date_info import PositionDateInfo
from src.xml_models.position_profile.position_detail.industry_code import IndustryCode
from src.xml_models.position_profile.position_detail.position_detail import PositionDetail
from src.xml_models.position_profile.position_detail.position_schedule import PositionSchedule
from src.xml_models.position_profile.position_detail.shift import Shift
from src.xml_models.position_profile.position_profile import PositionProfile
from src.xml_models.position_record_info import PositionRecordInfo
from src.xml_models.position_supplier import PositionSupplier
from src.xml_models.postal_address import PostalAddress
from src.xml_models.recipient import Recipient
import xml.dom.minidom

from src.xml_models.status_position import StatutPosition
from src.xml_models.supplier_id import SupplierId


def main():

    recipient = Recipient(
        organization_name="Henallux",
        person_name=PersonName(family_name="Briquet")
    )

    postal_address = PostalAddress(country_code='BE', postal_code='12345', recipient=recipient)

    physical_location = PhysicalLocation(postal_address=postal_address)

    # position_detail = PositionDetail(physical_locations=[physical_location, PhysicalLocation(postal_address=PostalAddress(country_code='FR', postal_code='43233'))])

    contact_henallux = ContactMethod(
        telephone=Telephone(
            subscriber_number='746846'
        ),
        internet_email_address='mdpbriar@henallux.be',
        internet_web_address='https://jobs.henallux.be',
        postal_address=postal_address,
    )

    position_opening = PositionOpening(
        position_record_info=PositionRecordInfo(
            id=IdOffre(id_owner='reour', id_value=5),
            status=StatutPosition(
                valid_to=datetime.strptime('2026-02-01', "%Y-%m-%d"),
                valid_from=date.today(),
                content="Active"
            )
        ),
        position_supplier=PositionSupplier(
            id=SupplierId(value='pouetou'),
            entity_name=EntityName(content="Pas de quartier"),
            contact_method=ContactMethod(
                telephone=Telephone(
                    subscriber_number='746846'
                ),
                internet_email_address='mdpbriar@henallux.be',
                internet_web_address='https://jobs.henallux.be',
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
                organization_name="Henallux",
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


            ),
        ),
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