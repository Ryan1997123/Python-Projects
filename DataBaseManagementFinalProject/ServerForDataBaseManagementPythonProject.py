#Ina Patrice Gonzales and Ryan Monaghan
#4 February 2020
#CISC4615
#Lab 1 Part 2
#server2.py

from socket import * 

serverPort = 12000 #server port number 
serverSocket = socket(AF_INET,SOCK_STREAM) #creates the socket 
serverSocket.bind(('localhost',serverPort)) #binds the socket 
serverSocket.listen(1) #calls the listeening function so the socket can listen for incoming connections 
print ('The server is ready to receive...')
while 1: #while loop that performs the sending and receiving of messages 
	connectionSocket, addr = serverSocket.accept() #accept the connection
	fromClient_hello = connectionSocket.recv(1024) #receives 'Hello Fordham' from Client
	fromServer_helloStudents = 'Server: Hello CIS Students'
	connectionSocket.send(fromServer_helloStudents.encode()) #sends out 'Hello CIS Students' from server
	fromClient_helloCISC = connectionSocket.recv(1024)  #receives 'Hello CISC4615' from client
	fromServer_bye = 'Server: Bye'
	connectionSocket.send(fromServer_bye.encode()) #sends out 'Bye' from server
	break
print ('Connection Closed.') 
connectionSocket.close() #closes the connection