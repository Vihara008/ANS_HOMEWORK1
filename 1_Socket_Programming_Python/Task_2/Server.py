import socket

from Config import *

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       

serverSocket.bind((ServerIp, Serverport))        

serverSocket.listen()  

counter = 0

client1Data=''

while True:  

    try:

        client, address = serverSocket.accept()  

        data = client.recv(1024).decode()

        counter = counter+1

        if(counter == 1):

            client1Data = data

        if data == '0':

            print('Exiting ....')

            serverSocket.close()

            break

        else:

            if(counter > 1):

                dataInInt = int(client1Data) 

                dataInInt = dataInInt - 1

                client.send(("\nClient 2 sent - "+data+"\nClient 1 sent - "+client1Data+"\nAfter transforming Client 1 data - "+ str(dataInInt)).encode())  

            else:

                client.send(("Thank you for sending - "+ data).encode())

    except Exception as e:

        print(e)

        client.send("Invalid input. Pleae try again".encode())  

        break