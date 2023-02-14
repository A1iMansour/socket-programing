import socket
import time

###                               MAC address????????????????????????????????????????????????????//

host= "10.169.21.212" #chosing host
port=1999  #port number 

csocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP

csocket.connect((host,port)) 

dest_address=input("what is the distination IP: ")

""""GET /hello.txt HTTP/1.1
User-Agent: curl/7.64.1
Host: www.example.com
Accept-Language: en, mi
client_socket.sendall(("GET / HTTP/1.1\r\n\r\nDestination: " + destination_ip).encode())

"""

request =input("what is your request: ")
print(f"request details:  | time: {time.ctime()}")
exct_time=time.ctime()
csocket.send(dest_address.encode('ascii'))
csocket.send(request.encode('ascii'))

print(csocket.recv(112).decode('ascii')+f" | exact time:{exct_time}")