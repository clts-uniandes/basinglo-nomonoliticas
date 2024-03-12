
from dataclasses import dataclass

from src.seedwork.application.commands import Command
from src.modules.users.application.dto import PersonalInformationAppDTO
from .base import SavePersonalInformationBaseHandler

from src.seedwork.application.commands import exec_command as command
from src.modules.users.domain.entities import PersonalInformation
from src.seedwork.infraestructure.uow import UnitOfWorkPort
from src.modules.users.application.mappers import MapperPersonalInformation
from src.modules.users.infrastructure.repositories import PersonalInformationRepository

@dataclass
class SavePersonalInfo(Command):
    id_credential: str
    email: str
    dni: str
    fullName: str
    phoneNumber: str

class SavePersonalInfoHandler(SavePersonalInformationBaseHandler):

    def handle(self, command: SavePersonalInfo):
        personal_information_dto = PersonalInformationAppDTO(id_credential=command.id_credential,email=command.email,
                                                             dni=command.dni,fullName=command.fullName,phoneNumber=command.phoneNumber)
        personal_information: PersonalInformation = self.personal_info_factory.create_object(personal_information_dto,
                                                                                             MapperPersonalInformation())
        personal_information.create_personal_info(personal_information)

        repository = self.repo_factory.create_object(PersonalInformationRepository.__class__)
        
        # if not full uow mode (caused ancestor called commit previously), better to clean up your batches copy
        UnitOfWorkPort.clean_old_batches()

        UnitOfWorkPort.register_batch(repository.add, personal_information)
        #UnitOfWorkPort.savepoint() only if full uow mode
        
        UnitOfWorkPort.commit()


@command.register(SavePersonalInfo)
def exec_command_save_personal_info(command: SavePersonalInfo):
    handler = SavePersonalInfoHandler()
    handler.handle(command)