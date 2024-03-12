import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from src.seedwork.infraestructure import utils
from src.modules.properties.infrastructure.schema.v1.commands import CommandUpdateProperty
from src.modules.properties.application.commands.update_property import UpdateProperty
from src.seedwork.application.commands import exec_command

def susbcribe_to_commands():
    client = None
    try:
        client = pulsar.Client(f'{utils.broker_host()}', authentication=pulsar.AuthenticationToken(utils.broker_token()))
        topic = 'event-update-property'
        full_topic = f'persistent://{utils.broker_tenant()}/{utils.broker_namespace()}/{topic}'
        consumer = client.subscribe(full_topic, consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-property', schema=AvroSchema(CommandUpdateProperty))

        while True:
            message = consumer.receive()
            
            try: 
                
                command_payload = message.value().data
                print(f'Command received: {command_payload}')
                property_id = command_payload.dni_tenant
                owner_id = command_payload.dni_landlord
                
                command = UpdateProperty(id=property_id, owner_id=owner_id)
                exec_command(command)
                
                consumer.acknowledge(message)
                
            except Exception as e:
                print(f'ERROR: processing topic! {e}')
        
    except:
        logging.error('ERROR: topic subscription!')
        traceback.print_exc()
        if client:
            client.close()
            
    finally:
        client.close()
            
