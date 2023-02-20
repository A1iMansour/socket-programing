import socket
import time

host= "10.169.20.37"#IP address for local host
port=9899

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket to accept connections

serv.bind((host,port))
serv.listen()


while True:
    csocket,address=serv.accept()#communication socket,each connection gets its socket

    #printing a message describing this request with the IP and exact time of the request
    print(f"Proxy server is connected to: {address}| time of request:{time.ctime()}\n")

    #incase error from client side
    try:
        request=csocket.recv(1024).decode('ascii')#recieving request
        dest_address=request[request.find("Host:")+6:(request).find("\r\n\r")]#taking address
        
    except ConnectionRefusedError:
        print("request not recieved from client\n")
        csocket.send("there was problem with your message\n")

   #actual time of request
    actual_time=time.ctime()

    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response=None
    try:#any error occuring here will be from  server side
        dest_socket.connect((dest_address, 80))
        
        #send the client's request to the destination server
        dest_socket.sendall(request.encode("ascii"))

        #printing the message with exact time of the actual request
        print(f"request recieved | actual time of request:{actual_time}\n")

        #receive the response from the destination server
        response = dest_socket.recv(1024).decode('ascii')
    except ConnectionRefusedError:
         print("server not responding\n")
         csocket.send("there was problem with the server,please try again".encode('ascii'))

    #printing a message that the response was received with the exact time
    print(f"response was recieved from server: {response}|  time of response:{time.ctime()}")

    #sending the client that response has been recieved
    csocket.send((f"respose {response}").encode('ascii'))
    print(f"response was send to client |time of response:{actual_time}\n")


    csocket.close()
    dest_socket.close()
    print("connection ended")

    
    

