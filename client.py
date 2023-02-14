import socket

host="127.0.0.1" #chosing host
port=1999  #port number for HTTP

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP

socket.connect((host,port)) 
request =input
socket.send(request.encode('ascii'))
print(socket.recv(112).decode('ascii'))