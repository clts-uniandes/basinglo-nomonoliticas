from src.config.db import db
from src.modules.users.domain.repositories import PersonalInformationRepository
from src.modules.users.domain.factories import PersonalInformationFactory
from src.modules.users.domain.entities import PersonalInformation
from src.modules.users.infrastructure.mappers import PersonalInformationMapper


class PersonalInformationPostgresRepository(PersonalInformationRepository): 
    

    def __init__(self):
        self._personal_information_factory: PersonalInformationFactory = PersonalInformationFactory()

    def add(self, personalInformation: PersonalInformation):
        session = db.session
        personal_information_dto = self._personal_information_factory.create_object(personalInformation, PersonalInformationMapper())
        session.add(personal_information_dto)