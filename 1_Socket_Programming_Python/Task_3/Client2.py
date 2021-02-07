import socket   

from Config import *     


2
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       

clientSocket.connect((ServerIp, Serverport))

letter = input("Enter Number :") 

clientSocket.sendall(letter.encode()) 

if(letter == '0'):

    clientSocket.close()

else:

    print (clientSocket.recv(1024).decode(),"\n") 

