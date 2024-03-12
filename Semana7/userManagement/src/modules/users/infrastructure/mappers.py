from .dto import PersonalInformation as PersonalInfoDTO
from .exceptions import NoImplementationForFactoryTypeException

from src.modules.users.domain.entities import PersonalInformation
from src.modules.users.domain.events import PersonalInfoCreated, PersonalInfoEvent
from src.seedwork.domain.repositories import Mapper
from src.seedwork.infraestructure.utils import time_millis

from .dto import PersonalInformation as PersonalInformationDTO

class UserEventsMapper(Mapper):

    versions = ('v1',)

    LATEST_VERSION = versions[0]

    # re-routes to the correct mapping method
    def __init__(self):
        self.router = {
            PersonalInfoCreated: self._entity_to_personal_info_created
        }

    def find_type(self) -> type:
        return PersonalInfoEvent.__class__

    def is_valid_version(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entity_to_personal_info_created(self, entity: PersonalInfoCreated, version=LATEST_VERSION):
        def v1(event):
            from .schema.v1.events import PersonalInfoCreatedPayload, PersonalInfoCreatedEvent
            payload = PersonalInfoCreatedPayload(
                id_credential = str(event.id_credential),
                email = str(event.email),
                created_at = str(event.created_at)
            )
            integration_event = PersonalInfoCreatedEvent(id=str(event.id))
            integration_event.id = str(event.id)
            integration_event.time = int(time_millis())
            integration_event.specversion = str(version)
            integration_event.type = 'PersonalInfoCreated'
            integration_event.datacontenttype = 'AVRO'
            integration_event.service_name = 'Users'
            integration_event.data = payload
            return integration_event
        if not self.is_valid_version(version):
            raise Exception(f'Version {version} was not able to be proccesed.')
        if version == 'v1':
            return v1(entity)

    def entity_to_dto(self, entity: PersonalInfoEvent, version=LATEST_VERSION) -> PersonalInfoDTO:
        if not entity:
            raise NoImplementationForFactoryTypeException
        func = self.router.get(entity.__class__, None)
        if not func:
            raise NoImplementationForFactoryTypeException
        return func(entity, version=version)

    def dto_to_entity(self, dto: PersonalInfoDTO) -> PersonalInformation:
        raise NotImplementedError

class PersonalInformationMapper(Mapper):
    
    def find_type(self) -> type:
        return PersonalInformation.__class__

    def entity_to_dto(self, entity: PersonalInformation) -> PersonalInformationDTO:
        personal_information_dto = PersonalInformationDTO()
        personal_information_dto.credentialId = entity.id_credential # pending de ver utilidad
        personal_information_dto.id = str(entity.id) # pending de ver utilidad
        personal_information_dto.fullName = entity.fullName
        personal_information_dto.dni = entity.dni
        personal_information_dto.email = entity.email
        personal_information_dto.phoneNumber = entity.phoneNumber
        return personal_information_dto

    def dto_to_entity(self, dto: PersonalInformationDTO) -> PersonalInformation:
        personal_information = PersonalInformation(id_credential=dto.credentialId,email=dto.email,dni=dto.dni,fullName=dto.fullName,phoneNumber=dto.phoneNumber)        
        return personal_information
    

