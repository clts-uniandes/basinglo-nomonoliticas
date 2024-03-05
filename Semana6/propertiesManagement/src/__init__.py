import threading

import src.modules.properties.infrastructure.consumers as properties

def start_consumer(app):
    threading.Thread(target=properties.susbcribe_to_commands, args=[app]).start()