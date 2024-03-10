from src.modules.sagas.seedwork.application.sagas import CoordinadorOrquestacion, Fin, Inicio, Transaccion
from src.modules.sagas.seedwork.dominio.eventos import EventoDominio
from src.modules.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandRemoveTransaction
from src.modules.transactions.infrastructure.schema.v1.events import EventTransactionCreated, EventTransactionFailed
from src.modules.properties.infrastructure.schema.v1.commands import CommandUpdateProperty, CommandUpdatePropertyPayload
from src.modules.properties.infrastructure.schema.v1.events import EventPropertyUpdated, EventPropertyUpdatedFailed

class ManagerTransaction(CoordinadorOrquestacion):

    def initializeSteps(self):
        self.steps = [
            Inicio(index=0),
            Transaccion(index=1, comando=CommandCreateTransaction, evento=EventTransactionCreated, error=EventTransactionFailed, compensacion=CommandRemoveTransaction),
            Transaccion(index=2, comando=CommandUpdateProperty, evento=EventPropertyUpdated, error=EventPropertyUpdatedFailed, compensacion=None),
            Fin(index=3)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        if isinstance(evento, EventTransactionCreated) and tipo_comando == CommandUpdateProperty:
            payload = CommandUpdatePropertyPayload(
                owner_id=evento.dni_landlord,
                id=evento.id_property,
            )
            return CommandUpdateProperty(data=payload)
        else:
            raise ValueError("event and commmand type not supported")



# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        manager = ManagerTransaction()
        manager.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")