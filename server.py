import socket

host= "127.0.0.1"#IP address for local host
port=1999

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket to accept connections
serv.bind((host,port))#binding host with port
serv.listen()


while True:
    csocket,address=serv.accept()#communication socket,each connection gets its socket
    print(f"Proxy server is connected to: {address}")
    message= csocket.recv(112).decode('ascii')
    print("message: "+message)
    csocket.send(("I got you").encode('ascii'))
    print("connection ended")

    
    

