import socket

host= "127.0.0.1" #chosing host
port=1999  #port number for HTTP

csocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP

csocket.connect((host,port)) 
request =input("type request: ")
csocket.send(request.encode('ascii'))
print(csocket.recv(112).decode('ascii'))