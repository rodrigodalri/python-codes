# sockets

Code for playing with Python’s ipaddress sockets.

Features:
- Echo Client and Server
- Multi-Connection Client and Server
 
### Echo 
The server will simply echo whatever it receives back to the client.

Checking funcionality Echo 
```
$ python3 echoserver.py 
Connected by ('127.0.0.1', 50538)

$ python3 echoclient.py 
Received b'Hello, world'
```

### Multi-Connection
Server and client that handles multiple connections using a selector object created from the selectors module.

Checking funcionality Multi-Connection 
```
$ python3 multiserver.py 127.0.0.1 8089 
listening on ('127.0.0.1', 8089)
accepted connection from ('127.0.0.1', 50710)
accepted connection from ('127.0.0.1', 50712)
echoing b'Message 1 from client.' to ('127.0.0.1', 50710)
accepted connection from ('127.0.0.1', 50714)
echoing b'Message 2 from client.' to ('127.0.0.1', 50710)
echoing b'Message 1 from client.Message 2 from client.' to ('127.0.0.1', 50712)
closing connection to ('127.0.0.1', 50710)
echoing b'Message 1 from client.Message 2 from client.' to ('127.0.0.1', 50714)
closing connection to ('127.0.0.1', 50712)
closing connection to ('127.0.0.1', 50714)

$ python3 multiclient.py 127.0.0.1 8089 3
starting connection 1 to ('127.0.0.1', 8089)
starting connection 2 to ('127.0.0.1', 8089)
starting connection 3 to ('127.0.0.1', 8089)
sending b'Message 1 from client.' to connection 1
sending b'Message 1 from client.' to connection 2
sending b'Message 1 from client.' to connection 3
sending b'Message 2 from client.' to connection 1
sending b'Message 2 from client.' to connection 2
sending b'Message 2 from client.' to connection 3
received b'Message 1 from client.' from connection 1
received b'Message 2 from client.' from connection 1
closing connection 1
received b'Message 1 from client.Message 2 from client.' from connection 2
closing connection 2
received b'Message 1 from client.Message 2 from client.' from connection 3
closing connection 3
```