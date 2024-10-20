from socket import *
# import chatroomClient
# import pickle
import parameters as p
from threading import Thread, Lock


class ChatroomServer:
    
    ############################--VARIABLES--#############################
    
    server_socket : socket = None
    
    
    stop_thread_flag : bool = False    # Flag for client removal
    socket_to_remove : socket = None   
    
    clients_sockets_dict : dict = dict() # Dictionary to store client socket as key and thread as value
    t_lock = Lock() # Lock for thread safety 
    
    
    #############################--METHODS--##############################
    
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
                
                # If message is empty, client has disconnected
                if not msg:
                    raise ConnectionResetError
                
                
                with self.t_lock: # Lock threads while accessing
                    
                    dead_clients = []  
                    for client in self.clients_sockets_dict.keys():
                        try:
                            client.send(msg.encode())
                        # Mark socket for removal if socket is dead
                        except:
                            dead_clients.append(client)
                    
                    # Remove dead clients
                    for dead_client in dead_clients:
                        try:
                            dead_client.close()
                            self.clients_sockets_dict.pop(dead_client)
                        except:
                            pass
                
            # Disconnects client by setting socket to remove and raise stop_thread_flag 
            except ConnectionResetError:
                with self.t_lock: # Lock threads while accessing
                    self._client_removal_setup(f"Client disconnected", cli_soc)
                break

            # Handle any other socket errors
            except error as e:
                with self.t_lock: # Lock threads while accessing
                    self._client_removal_setup(f"Error: {e}", cli_soc)
                break
                
    def _client_removal_setup(self, err_msg : str, client_soc : socket):
        """
        Process to remove clients from server

        Args:
            err_msg (str): Reason for calling function
            client_soc (socket): client socket to remove
        """
        print(err_msg)
        self.socket_to_remove = client_soc
        self.stop_thread_flag = True
                
                

           
            


        

