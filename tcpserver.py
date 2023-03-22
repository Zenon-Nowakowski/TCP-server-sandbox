# This is tcpserver.py file
import socket                                         
from substitution_functions import * 
# create a TCP/IP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# my IP 
host = "IP"                         

#set port number for this server
port = 10000                                          

# bind to the port
serversocket.bind((host, port))

# Listen for incoming connections, queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # wait for a connection
   print('waiting for a connetion on port ' + str(port) + '\n')
   clientsocket,addr = serversocket.accept()      

   #Confirm connection to client
   print("Got a connection from " + str(addr))
   #Collect data from client
   data = clientsocket.recv(1024)
   #if statement for recieving data 
   if data: 
      print("recieved: " + data.decode())
      reply = '...'
      reply= data.decode()
      #decode sbox encrpytion
      inv_sBox(reply)
      clientsocket.send(reply.encode())
      break
   else:
      print('no more data from' + str(addr))
      break

   clientsocket.close()
