import socket   

from Config import *     



clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       

clientSocket.connect((ServerIp, Serverport))

letter = input("Enter Number :") 

clientSocket.sendall(letter.encode()) 

if(letter == '0'):

    clientSocket.close()

else:

    print ("Server sent - ",clientSocket.recv(1024).decode(),"\n") 

