import socket
import time
import uuid


host= "10.169.23.15" #chosing host
port=9899  #port number 

csocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP

csocket.connect((host,port)) 

dest_address=input("what is the distination IP: ")

""""GET /hello.txt HTTP/1.1
User-Agent: curl/7.64.1
Host: www.example.com
Accept-Language: en, mi
client_socket.sendall(("GET / HTTP/1.1\r\n\r\nDestination: " + destination_ip).encode())

"""
request="hi"##################
##request =input("what is your request: ")#######################
print(f"request details:{request}  | time: {time.ctime()}")

start = time.time()#to get round trip time

exact_time=time.ctime()
csocket.send(dest_address.encode('ascii'))
csocket.send(request.encode('ascii'))

print(f"{csocket.recv(1024).decode('ascii')} | exact time:{exact_time}\n")
end=time.time()#to get round trip time
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))