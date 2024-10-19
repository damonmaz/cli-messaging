import chatroomClient
from threading import Thread
from datetime import datetime
from socket import *

def main():
    # Enter username and connect to server
    name = input("Please input username: ")
    client = chatroomClient.ChatroomClient(username=name)
    client.connect_to_server()
    
    t = Thread(target=client.listen_for_messages)
    t.daemon = True # thread ends whenever the main thread ends
    t.start()
    
    while True:
        # Try to get client message, add date and send to server
        try:
            
            client_message = input("MSG: ")
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            
            client_message = f"[{date}] {client.client_username}: {client_message}"
            
            client.client_socket.send(client_message.encode())
        
        # Shut down client with Keyboard Interrupt
        except KeyboardInterrupt:
            client.client_socket.close()
            break 


if __name__ == "__main__":
    main()