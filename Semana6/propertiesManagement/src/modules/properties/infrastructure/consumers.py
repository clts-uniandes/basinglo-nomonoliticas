import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from src.seedwork.infraestructure import utils
from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction
from src.modules.properties.application.commands.update_property import UpdateProperty
from src.seedwork.application.commands import exec_command

def susbcribe_to_commands(app=None):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('topic_transaction', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-transaction-commands', schema=AvroSchema(CommandCreateTransaction))

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
            
