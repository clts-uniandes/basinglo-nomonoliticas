import threading
import src.modules.auth.infrastructure.consumers as auth

auth.subscribe_to_events()
