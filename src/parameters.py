from enum import Enum

class ServerParameters(Enum):
    SERVER_ADDRESS = "127.0.0.1" 
    SERVER_PORT = 5001
    SERVER_NAME = "SERVER"
    
class ClientParameters(Enum):
    DEFAULT_NAME = "default"