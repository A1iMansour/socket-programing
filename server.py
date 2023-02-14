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
    print(f"Proxy server is connected to: {address}| time of request:{time.ctime()}")

    #incase error from client side
    try:
        request=csocket.recv(112)
    except ConnectionRefusedError:
        print("Message not recieved from client")
        csocket.send("there was problem with your message")

    message= request.decode('ascii')
    actual_time=time.ctime()

    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:#any error occuring here will be from  server side
        dest_socket.connect(("www.google.com", 80))

        #send the client's request to the destination server
        dest_socket.sendall(request)

        #printing the message with exact time of the actual request
        print(f"message recieved: {message}| actual time of request:{actual_time}".encode('ascii'))

        #receive the response from the destination server
        response = dest_socket.recv(1024).decode('ascii')
    except ConnectionRefusedError:
         print("server not responding")
         csocket.send("there was problem with the server,please try again")

    #printing a message that the response was received with the exact time
    print(f"response was recieved from server: {response}|  time of response:{actual_time}".encode('ascii'))

    #sending the client that response has been recieved
    csocket.send((f"respose {response}|  time of request:{time.ctime()}").encode('ascii'))
    print(f"response was send to client |time of response:{actual_time}.encode('ascii')")


    csocket.close()
    dest_socket.close()
    print("connection ended")

    
    

