from src.seedwork.domain.repositories import Mapper
from src.modules.users.domain.entities import PersonalInformation
from .dto import PersonalInformation as PersonalInformationDTO

class PersonalInformationMapper(Mapper):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def find_type(self) -> type:
        return PersonalInformation.__class__

    def entity_to_dto(self, entity: PersonalInformation) -> PersonalInformationDTO:
        
        personal_information_dto = PersonalInformationDTO()
        personal_information_dto.id = str(entity.id)
        personal_information_dto.userName = entity.userName
        personal_information_dto.fullName = entity.fullName
        personal_information_dto.dni = entity.dni
        personal_information_dto.email = entity.email
        personal_information_dto.phoneNumber = entity.phoneNumber
        personal_information_dto.password = entity.password 
        personal_information_dto.createdAt = entity.createdAt  
        return personal_information_dto


    def dto_to_entity(self, dto: PersonalInformationDTO) -> PersonalInformation:
        personal_information = PersonalInformation(id=dto.id, createdAt=dto.createdAt, userName=dto.userName, fullName = dto.fullName, dni = dto.dni, email = dto.email, phoneNumber = dto.phoneNumber,  password = dto.password)        
        return personal_information
