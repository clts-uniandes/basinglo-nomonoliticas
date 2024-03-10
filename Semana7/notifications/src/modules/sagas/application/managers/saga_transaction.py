from src.modules.sagas.seedwork.application.sagas import CoordinadorOrquestacion, Fin, Inicio, Transaccion
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration
from src.modules.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandRemoveTransaction, CommandCreateTransactionPayload
from src.modules.transactions.infrastructure.schema.v1.events import EventTransactionCreated, EventTransactionFailed
from src.modules.properties.infrastructure.schema.v1.commands import CommandUpdateProperty, CommandUpdatePropertyPayload
from src.modules.properties.infrastructure.schema.v1.events import EventPropertyUpdated, EventPropertyUpdatedFailed
from src.modules.notifications.infrastructure.schema.v1.commands import CommandCreateNotification, CommandReverseNotification, CommandCreateNotificationPayload
from src.modules.notifications.infrastructure.schema.v1.events import EventNotificationCreated, EventNotificationFailed

class ManagerTransaction(CoordinadorOrquestacion):

    def initializeSteps(self):
        self.steps = [
            Inicio(index=0),
            Transaccion(index=1, comando=CommandCreateNotification, evento=EventNotificationCreated, error=EventNotificationFailed, compensacion=CommandReverseNotification),
            Transaccion(index=2, comando=CommandCreateTransaction, evento=EventTransactionCreated, error=EventTransactionFailed, compensacion=CommandRemoveTransaction),
            Transaccion(index=3, comando=CommandUpdateProperty, evento=EventPropertyUpdated, error=EventPropertyUpdatedFailed, compensacion=None),
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

    def construir_comando(self, evento: EventIntegracion, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        
        if isinstance(evento, EventNotificationCreated) and tipo_comando == CommandCreateTransaction:
            payload = CommandCreateTransactionPayload(
                dni_landlord = evento.dni_landlord,
                dni_tenant = evento.dni_tenant,
                id_property = evento.id_property,
                monetary_value = evento.monetary_value,
                contract_initial_date = evento.contract_initial_date,
                contract_final_date = evento.contract_final_date,
            )
            return CommandCreateTransaction(data=payload)
        
        elif isinstance(evento, EventTransactionCreated) and tipo_comando == CommandUpdateProperty:
            payload = CommandUpdatePropertyPayload(
                owner_id=evento.dni_landlord,
                id=evento.id_property,
            )
            return CommandUpdateProperty(data=payload)            
        
        # COMPENSATION---------------------------------------------------------------------------------------------------------------------------

        elif isinstance(evento, EventPropertyUpdatedFailed) and tipo_comando == CommandRemoveTransaction:
            payload = CommandCreateTransactionPayload(
                dni_landlord = evento.dni_landlord,
                dni_tenant = evento.dni_tenant,
                id_property = evento.id_property,
                monetary_value = evento.monetary_value,
                contract_initial_date = evento.contract_initial_date,
                contract_final_date = evento.contract_final_date,
            )
            return CommandRemoveTransaction(data=payload)

        elif isinstance(evento, EventTransactionFailed) and tipo_comando == CommandReverseNotification:
            payload = CommandCreateNotificationPayload(
                dni_landlord = evento.dni_landlord,
                dni_tenant = evento.dni_tenant,
                id_property = evento.id_property,
                monetary_value = evento.monetary_value,
                contract_initial_date = evento.contract_initial_date,
                contract_final_date = evento.contract_final_date,
            )
            return CommandReverseNotification(data=payload)

        else:
            raise ValueError("event and commmand type not supported")

    # TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
    def oir_mensaje(mensaje):
        if isinstance(mensaje, EventIntegracion):
            manager = ManagerTransaction()
            manager.procesar_evento(mensaje)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
