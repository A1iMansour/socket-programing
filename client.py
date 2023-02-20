import socket
import time
import uuid


host= "10.169.20.37" #chosing host
port=9899  #port number 

csocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP

csocket.connect((host,port)) 

dest_address=input("what is the destination IP: ")
request=f"GET /index.html HTTP/1.1\r\nHost: {dest_address}\r\n\r\n".encode("utf-8")
time_of_request=time.ctime()
csocket.send(request)


print(f"request details:{request}  | time: {time_of_request}")

start = time.time()#to get round trip time
recieve=csocket.recv(1024).decode('ascii')#recieve reply
exact_time=time.ctime()#getting exact time

#recieving response and printing
print( f"{recieve} | exact time:{exact_time}\n")
end=time.time()#to get round trip time

#getting MAC addres
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))