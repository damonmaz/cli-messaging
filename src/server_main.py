from chatroomServer import ChatroomServer
from threading import Thread


def main():

    # Create server
    server = ChatroomServer()
    # Queue of 5 users
    server.server_socket.listen(5) 
    
    print(f"[{server.server_name}]: Awaiting Users") 
    
    while True:
        # we keep listening for new connections all the time
        client_socket, client_address = server.server_socket.accept()
        print(f"[+] {client_address} connected.")
        # add the new connected client to connected sockets
        server.set_clients_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=server.client_propagate, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

if __name__ == "__main__":
    main()