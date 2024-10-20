import chatroomServer
from threading import Thread
import parameters as p
from socket import *


def main():

    server = chatroomServer.ChatroomServer()
    
    server.server_socket.listen(100) 
    
    print(f"{p.ServerParameters.SERVER_NAME.value}: Awaiting Users") 
    
    # Continually listen for new connections
    while True:
        
        # Check is client needs to be removed
        if server.stop_thread_flag is True:
            # Lock threads while accessing
            with server.t_lock: # Lock threads while accessing 
                try:
                    # Get the thread associated with the socket, close and remove from dict
                    if server.socket_to_remove in server.clients_sockets_dict:
                        server.socket_to_remove.close()
                        server.clients_sockets_dict.pop(server.socket_to_remove)
                except:
                    pass
                
                # Reset flags
                server.socket_to_remove = None
                server.stop_thread_flag = False
            
        
        try:
            # Accept new client
            client_socket, client_address = server.server_socket.accept()
            print(f"[+] {client_address} connected.")

            # start a new thread that listens for each client's messages
            thread = Thread(target=server.client_propagate, args=(client_socket,))
            thread.daemon = True # thread ends whenever the main thread ends
            thread.start()
            
            # Set key as client socket and its thread as its value
            with server.t_lock: # Lock threads while accessing
                server.clients_sockets_dict[client_socket] = thread
        
        # Disconnect clients, stop threads, and shut down server and with Keyboard Interrupt
        except KeyboardInterrupt:
            print("\nShutting down server...")
            
            with server.t_lock: # Lock threads while accessing
                # Close client sockets
                for client in list(server.clients_sockets_dict.keys()):
                    try:
                        client.close()
                    except:
                        pass
                    
            # Close server socket
            server.server_socket.close()
            break
            
        except Exception as e:
            print(f"Error in main loop: {str(e)}")
            continue
    
     

if __name__ == "__main__":
    main()