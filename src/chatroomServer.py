from socket import *
# import chatroomClient
# import pickle
import parameters as p


class ChatroomServer:
    
    ############################--VARIABLES--#############################
    
    #---------------------------PUBLIC VARIABLES-------------------------#
    
    
    server_socket : socket = None
    
    set_clients_sockets : set = set()
    
    
    #############################--METHODS--##############################
    
    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_Constructors_-_-_-_-_-_-_-_-_-_-_-_-_-#
    
    def __init__(self):
        """
        Create socket and bind to default host address and port (127.0.0.1, 5001)
        
        Args:
            None
            
        """
        
        # Set up server socket
        # (IPv4, TCP)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
        self.server_socket.bind((p.ServerParameters.SERVER_ADDRESS.value, p.ServerParameters.SERVER_PORT.value))
        
    def client_propagate(self, cli_soc: socket):
        """
        Propograte message sent by client to all other clients

        Args:
            cli_soc (socket): The client socket whose message is being propogates to all other clients
        """

        while True:
            # Client message
            try:
                # msg = cli_soc.client_socket.recv(1024).decode()
                msg = cli_soc.recv(1024).decode()
                
                # Send message from client to all other clients
                for c in self.set_clients_sockets:
                    c.send(msg.encode())
                
            # Client disconnect
            except Exception as e:
                # print(f"{cli_soc.CLIENT_NAME} disconnected.")
                print("Client disconnected")
                self.set_clients_sockets = set().remove(cli_soc)

           
            


        

