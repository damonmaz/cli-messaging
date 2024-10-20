from socket import *
import parameters as p

class ChatroomClient:
    
    ############################--VARIABLES--#############################

    #---------------------------PUBLIC VARIABLES-------------------------#
    
    client_username = p.ClientParameters.DEFAULT_NAME.value
    
    client_socket : socket = None
    
    
    #############################--METHODS--##############################
    
    def __init__(self, username : str):
        """
        Create client socket and set username

        Args:
            name (str): username of client
        """
        
        self.client_username = username
        self.client_socket = socket()
        self.client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
    
    def connect_to_server(self):
        """
        Connect to server, close socket and exit if error
        """
        print(f"Connecting to {p.ServerParameters.SERVER_ADDRESS.value}:{p.ServerParameters.SERVER_PORT.value}...")
        
        # Try connecting
        try:
            self.client_socket.connect((p.ServerParameters.SERVER_ADDRESS.value, p.ServerParameters.SERVER_PORT.value))
            print("Connected!")
        
        # Raise error and exit if unable to connect
        except:
            print(f"\mCould not connect to {p.ServerParameters.SERVER_ADDRESS.value}:{p.ServerParameters.SERVER_PORT.value}")
            print("Terminating client...")
            self.client_socket.close()
            exit(1)
    
    
    def listen_for_messages(self):
        """
        Recieve messages from other clients through server
        """
        
        while True:
            try:
                message = self.client_socket.recv(2048).decode()
                print("\n" + message)
                
            except ConnectionResetError:
                print("Connection to server terminated")
                exit(1)
                
            except ConnectionAbortedError:
                print("Disconnected from server")
                exit(1)
                