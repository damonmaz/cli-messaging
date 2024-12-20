import chatroomClient
from threading import Thread
from datetime import datetime
from socket import *  
from profanity import has_profanity, censor_profanity
import random
import parameters as p
from colorama import Fore, init
import time

def main():
    
    # Variables
    init() # Initialize colorama
    text_color = random.choice(p.color_list)
    name : str = ""
    client_message : str = ""
    client : chatroomClient = None
    t : Thread = None
    start_time : float = 0 # Used to measure how long it has been since client last sent message
    stop_time : float = 0
    slow_down_counter : int = 0

    # Enter username
    while True:
        try:
            name = input("Please input username: ")

            # Check for profanity in name
            if has_profanity(name):
                print(f"{Fore.RED}Inappropiate name. Try again{Fore.RESET}")
                continue

            # Check that name is not more than 50 chars
            if (len(name) > 50 or len(name) < 1 or len(name.replace(' ', '')) < 1):
                print(f"{Fore.RED}Minimum of 0 characters or maximum of 50 characters for a name. Try again{Fore.RESET}")
                continue

            break
        
        except KeyboardInterrupt:
            exit(1)
            
        except:
            exit(1)
    
    # Create client and connect to server
    client = chatroomClient.ChatroomClient(username=name)
    client.connect_to_server()
    
    # Start thread for listening for messages
    t = Thread(target=client.listen_for_messages)
    t.daemon = True # thread ends whenever the main thread ends
    t.start()
    
    # Send welcome message
    client.client_socket.send(f"{Fore.WHITE}{client.client_username} has connected{Fore.RESET}".encode())
    
    while True:
        # Try to get client message, add date and send to server
        try:
            while True:
                
                # Check if client is spamming
                if start_time != 0:
                    stop_time = time.time()
                    
                    if stop_time - start_time < 0.1:
                        print(f"{Fore.RED}Slow down...{Fore.RESET}")
                        slow_down_counter += 1
                        
                        # Kick if they have spammed over 15 times
                        if slow_down_counter > 15:
                            print(f"{Fore.RED}You have been kicked for spamming{Fore.RESET}")
                            raise KeyboardInterrupt
                        
                        time.sleep(1)
                
                start_time = time.time()
                
                client_message = input()
                
                # Remove client_message that was just typed
                print('\033[1A' + '\033[K', end='')
                
                # Make sure client message is not more than 2048 bytes long
                # (Max bits server can handle is 2048)
                if len(client_message.encode('utf-8')) > 2048:
                    print(f"{Fore.RED}Message was not sent because it was too long{Fore.RESET}")
                    continue

                break
        
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            
            client_message = censor_profanity(client_message)
            client_message = f"{text_color}[{date}] {client.client_username}: {client_message}{Fore.RESET}"
            
            client.client_socket.send(client_message.encode())
        
        # Shut down client with Keyboard Interrupt
        except KeyboardInterrupt:
            if ConnectionResetError:
                exit(1)
            client.client_socket.send(f"{Fore.WHITE}[{date}]: {client.client_username} has disconnected{Fore.RESET}".encode())
            time.sleep(0.25) # Need this delay or the server crashes
            client.client_socket.close()
            break 
        
        except ConnectionResetError:
            exit(1)

if __name__ == "__main__":
    main()