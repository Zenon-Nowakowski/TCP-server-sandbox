# This is tcpclient.py file

import socket
from substitution_functions import * 
# create a TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# update with the IP address of your server
host = "192.168.0.15"
#print to make sure it has an IP address
print(host)

# set destination port
port = 10000

# connection to hostname on the port.
s.connect((host, port))

# send message. The string needs to be converted to bytes. old code below
# blueTeam = ["Ana ", "Emily ", "Micheal ", "John ", "Ben "]
# for player in blueTeam: 
#     s.send(player.encode())
#Example of using sBox encryption
plaintext = "Zoo xray rellis college station csci458"
msg = sBox(plaintext)
s.send(msg.encode())

# Receive no more than 1024 bytes
reply = s.recv(1024)

print("ECHO: " + reply.decode())

# Close connection
s.close()

