from src.seedwork.domain.repositories import Mapper
from src.modules.users.domain.entities import PersonalInformation
from .dto import PersonalInformation as PersonalInformationDTO

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
    

