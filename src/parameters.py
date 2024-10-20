from enum import Enum
from colorama import Fore

# Colors of text
color_list = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
]


class ServerParameters(Enum):
    """
    Server parameters
    """
    
    SERVER_ADDRESS = "127.0.0.1" 
    SERVER_PORT = 5001
    SERVER_NAME = "SERVER"
    
class ClientParameters(Enum):
    """
    Client parameters
    """
    DEFAULT_NAME = "default"