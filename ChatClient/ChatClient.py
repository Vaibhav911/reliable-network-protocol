#######################################################
#		PEER TO PEER CHAT  APLLICATION 
######################################################

#Importing libraries
import datetime
import socket
import threading
import sys
import select 

#Message class
class Message:

	#message recieved 
	rcvd = False 
	#sequence number of the message
	sqn_num = 0 

	def __init__(self,msg):
		self.msg = msg 

	#function to retreive the sequence number of message
	def get_sqn_num(self):
		print("get from protocol")


#default IP Address and Port
IPADDR = "127.0.0.1"
PORT   = 9000

#send message function to keep on sending messages 
def sendMessage(sock):
	print(sock)

	while True :
		connection,addr = sock.accept()
		inputString = input(str("\nOutgoing : "))
		message = Message(inputString)
		msg = message.msg
		connection.sendall(msg.encode('ascii'))

	connection.close()

#recieve message function to keep on recieving messages
def rcvMessage():
	sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
	sock.connect((IPADDR,PORT))

	while True:
		msg = sock.recv(4096)
		msg = msg.decode('ascii')
		print("\nIncoming : "+msg)

	sock.close()


if __name__ == '__main__':

	#Creating the socket descriptor
	try:
		sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
	except socket.error as error:
		print("Sorry, Socket couldn't be created.")
		sys.exit()

	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	

	try:
		sock.bind((IPADDR,PORT))
	except socket.error:
		print("Binding Failed!")
		sys.exit()


	sock.listen(1)
	print('Listening at', sock.getsockname())

	sendingThread = threading.Thread(target=sendMessage,args=(sock,))
	recievingThread = threading.Thread(target=rcvMessage)

	sendingThread.start()
	recievingThread.start()


	sendingThread.join()
	recievingThread.join()

	print("Peer Exiting!")
