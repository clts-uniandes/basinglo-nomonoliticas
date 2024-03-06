from src.seedwork.application.dto import Mapper as AppMap
from src.seedwork.domain.repositories import Mapper as RepoMap
from src.modules.users.domain.entities import PersonalInformation
from .dto import PersonalInformationAppDTO

class MapperUsersDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> PersonalInformationAppDTO:
        print(">>>>>ID de credencial recibida:    ",external['id_credential'],)
        personal_info_dto = PersonalInformationAppDTO(
            id_credential = external['id_credential'],
            email = external['email'],
            dni = external['dni'],
            fullName = external['fullName'],
            phoneNumber = external['phoneNumber']
        )
        return personal_info_dto

    def dto_to_external(self, dto: PersonalInformationAppDTO) -> dict:
        return dto.__dict__

class MapperPersonalInformation(RepoMap):

    def find_type(self) -> type:
        return PersonalInformation.__class__
        
    def entity_to_dto(self, entity: PersonalInformation) -> PersonalInformationAppDTO:
        return PersonalInformationAppDTO(entity.id_credential,entity.email,entity.dni,entity.fullName,entity.phoneNumber)

    def dto_to_entity(self, dto: PersonalInformationAppDTO) -> PersonalInformation:
        personal_information = PersonalInformation()
        personal_information.id_credential = dto.id_credential
        personal_information.email = dto.email
        personal_information.dni = dto.dni
        personal_information.fullName = dto.fullName
        personal_information.phoneNumber = dto.phoneNumber

        return personal_information



