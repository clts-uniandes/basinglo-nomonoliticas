from src.config.db import db
from uuid import UUID

from src.modules.users.domain.repositories import PersonalInformationRepository
from src.modules.users.domain.factories import PersonalInformationFactory
from src.modules.users.domain.entities import PersonalInformation
from .mappers import PersonalInformationMapper

class PersonalInformationPostgresRepository(PersonalInformationRepository):

    def __init__(self):
        self._personal_information_factory: PersonalInformationFactory = (
            PersonalInformationFactory()
        )

    @property
    def credential_factory(self):
        return self._personal_information_factory

    def get_by_id(self, id: UUID) -> PersonalInformation:
        raise NotImplementedError

    def add(self, personalInformation: PersonalInformation):
        personal_information_dto = self._personal_information_factory.create_object(
            personalInformation, PersonalInformationMapper()
        )
        db.session.add(personal_information_dto)
