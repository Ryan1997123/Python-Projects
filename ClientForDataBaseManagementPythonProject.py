#Ina Patrice Gonzales and Ryan Monaghan
#4 February 2020
#CISC4615
#Lab 1 Part 2
#client2.py

from socket import *

serverName = 'localhost' #server's name 
serverPort = 12000 #server's port number 
clientSocket = socket(AF_INET, SOCK_STREAM) #creates the socket 
clientSocket.connect((serverName,serverPort)) #makes the connection
messages = [] #list that stores all of the messagese sent between the client and server 

fromClient_hello = 'Client: Hello Fordham'
messages.append(fromClient_hello) #appends 'Client: Hello Fordham' to messages list
clientSocket.send(fromClient_hello.encode()) #sends 'Hello Fordham' to server 

fromServer_students = clientSocket.recv(1024) #receives 'Server: Hello CIS Students' message from server
messages.append(fromServer_students.decode('utf-8')) #appends 'Server: Hello CIS Students' into a list

fromClient_helloCISC = 'Client: Hello CISC4615'
messages.append(fromClient_helloCISC) #appends 'Client: Hello CISC4615' to messages list 
clientSocket.send(fromClient_helloCISC.encode()) #sends out 'Cient: Hello CISC4615' from client

fromServer_bye = clientSocket.recv(1024) #receives 'Server: Bye' message from the server 
messages.append(fromServer_bye.decode('utf-8')) #appends 'Server: Bye' to meessages list 

print ('Connection Closed.') #outputs that the connection is closed 
clientSocket.close() #closes the connection

print ('This is the chat from the server and the client:')
print("\n".join(messages)) #prints out the messages list that has the messages sent and received from client