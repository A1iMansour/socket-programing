import socket
import time

host= "10.169.21.212"#IP address for local host
port=1999

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket to accept connections
serv.bind(('',port))#binding host with port,''used so the socket won't be to stricted
serv.listen()


while True:
    csocket,address=serv.accept()#communication socket,each connection gets its socket

    #printing a message describing this request with the IP and exact time of the request
    print(f"Proxy server is connected to: {address}| time of request:{time.ctime()}\n")

    #incase error from client side
    try:
        dest_address=csocket.recv(112)#taking address
        request=csocket.recv(112)#taking request
    except ConnectionRefusedError:
        print("Message not recieved from client\n")
        csocket.send("there was problem with your message\n")

    message= request.decode('ascii')
    actual_time=time.ctime()

    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:#any error occuring here will be from  server side
        dest_socket.connect((dest_address.decode('ascii'), 80))#connect method will automatically translate string to its IP address

        #send the client's request to the destination server
        dest_socket.sendall(f"GET / HTTP/1.1\r\nHost:{dest_address}\r\n\r\n".encode('ascii'))

        #printing the message with exact time of the actual request
        print(f"request recieved: {message}| actual time of request:{actual_time}\n")

        #receive the response from the destination server
        response = dest_socket.recv(1024).decode('ascii')
    except ConnectionRefusedError:
         print("server not responding\n")
         csocket.send("there was problem with the server,please try again")

    #printing a message that the response was received with the exact time
    print(f"response was recieved from server: {response}|  time of response:{time.ctime()}".encode('ascii'))

    #sending the client that response has been recieved
    csocket.send((f"respose {response}|  time of request:{time.ctime()}").encode('ascii'))
    print(f"response was send to client |time of response:{actual_time}\n")


    csocket.close()
    dest_socket.close()
    print("connection ended")

    
    

