# CLI Chatroom

## Overview
A chatroom application where clients can connect to a server and chat with each other.

I made this as a side-projectto practice using TCP sockets and threading.

## Implementation Details
- Uses TCP (Transmission Control Protocol) sockets for communication between server and clients
- Implements threading for concurrent sending and receiving of messages
- Includes a profanity filters and checks to make sure messages and usernames meet packet size requirements

## Requirements
- Python 3.x
- colorama module
```
pip install colorama
```
- filter-profanity module
```
pip install filter-profanity
```

## Usage

### Change Parameters
Parameters of the server and client, such as the name of the server, the server IP address or server port number, can be changed in parameters.py

### Run the Program
In the command line interface, one instance of the server should be run and many clients can be run.

Run server:

```
python server_main.py
```

Run client:

```
python client_main.py
```

# Author
Damon Mazurek
