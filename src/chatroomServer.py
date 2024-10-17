from socket import *
import ChatroomClient
import pickle


class ChatroomServer:
    
    ############################--VARIABLES--#############################
    
    #--------------------------PRIVATE VARIABLES-------------------------#
                                                                       
    _server_host_addr : str = "127.0.0.1"                                          
    _server_port : int = 5001

    
    #---------------------------PUBLIC VARIABLES-------------------------#
    
    server_name : str = "SERVER"
    
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
        self.server_socket.bind((self._server_host_addr, self._server_port))
        
    # def __init__(self, given_host_addr: str, given_server_port: int):
    #     """
    #     Create socket and bind to given host address and port 

    #     Args:
    #         given_host_addr (str): Host address 
    #         given_server_port (int): Host port
            
    #     """
    #     # Set up server socket
    #     # (IPv4, TCP)
    #     self.server_socket = socket(AF_INET, SOCK_STREAM)
    #     self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    #     self.server_socket.bind((given_host_addr, given_server_port))
        
    def client_propagate(self, cli_soc: socket):

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

           
            


        

