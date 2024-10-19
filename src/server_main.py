import chatroomServer
from threading import Thread
import parameters as p


def main():

    server = chatroomServer.ChatroomServer()
    
    # Queue of 5 users
    server.server_socket.listen(5) 
    
    print(f"{p.ServerParameters.SERVER_NAME.value}: Awaiting Users") 
    
    # Continually listen for new connections
    while True:
        
        try:
            # Accept new client
            client_socket, client_address = server.server_socket.accept()
            print(f"[+] {client_address} connected.")
            server.set_clients_sockets.add(client_socket)

            # start a new thread that listens for each client's messages
            t = Thread(target=server.client_propagate, args=(client_socket,))
            t.daemon = True # thread ends whenever the main thread ends
            t.start()
        
        # Shut down server and disconnect clients with Keyboard Interrupt
        except KeyboardInterrupt:
            for c in server.set_clients_sockets:
                c.close()
            server.server_socket.close() 
            exit(1) 
    
     

if __name__ == "__main__":
    main()