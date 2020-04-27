#######################################################
#		PEER TO PEER CHAT  APLLICATION 				  #
#######################################################

#Importing libraries
import datetime
import socket
import threading
import sys
import select 
import time

sys.path.append("../Protocol")
from ReliableUDPSocket import ReliableUDPSocket


#send message function to keep on sending messages 
def sendMessage(skt):
	global signal
	while signal:
		inputString = input(str("\nOutgoing : "))
		if inputString == "quit" or inputString == "q":
			signal = False
		else:
			skt.send(inputString)

#recieve message function to keep on recieving messages
def rcvMessage(skt):
	global signal
	while signal:
		msg = skt.recv()
		if (msg != -1):
			print("\nIncoming : "+msg)
		time.sleep(0.5)

if __name__ == '__main__':

	host_IP = input(str("Enter your friend's IP: "))
	#Creating the socket descriptor
	try:
		skt = ReliableUDPSocket(host_IP, 5001, host_IP, 5000)
	except socket.error as error:
		print("Sorry, Socket couldn't be created.")
		sys.exit()

	global signal 
	signal = True

	sendingThread = threading.Thread(target=sendMessage, args=(skt,))
	recievingThread = threading.Thread(target=rcvMessage, args=(skt,))

	sendingThread.start()
	recievingThread.start()

	sendingThread.join()
	recievingThread.join()


	print("Peer Exiting!")
