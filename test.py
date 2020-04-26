import socket
import threading
import time

class Packet:
	'''
	This is the structure of packet stored in the
	all the buffers.
	'''
	ack_rcvd = False
	seq_num = 0
	data = ""
	type = 0
	# type 0 is for data packet, type 1 is for ACK packet.

	def __init__(self, data, seq_num, type):
		self.data = data
		self.seq_num = seq_num
		self.type = type

class ReliableUDPSocket:
	'''
	A reliable protocol based on UDP using selective repeat.
	'''
	# Initialize necessary buffers for sending data packets, 
	# ACK packets and receiving packets
	send_buff = []
	send_buff_ACK = []
	recv_buff = []

	# Create a UDP socket.
	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	# Sequence number for sending and receiving space.
	seq_num_send = 0
	seq_num_recv = 0

	cwnd_size = 10

	#length_of_sent_object
	length=0
	
	def __init__(self, src_IP, src_port, dest_IP, dest_port):
		# Set user given source IP address and source port
		self.src_IP = src_IP
		self.src_port = src_port
		self.sock.bind((self.src_IP, self.src_port))

		# Set destination IP addr and port as given by user.
		self.host_addr = (dest_IP, dest_port)
		print("socket created", self.sock)

		# signal attribute is for controlling threads, if false, threads will stop.
		self.signal = True
		# Create and start all threads for sending and receiving data through ports.
		self.send_thread = threading.Thread(target=self.send_thread_util, daemon=True)
		self.recv_thread = threading.Thread(target=self.recv_thread_util, daemon=True)
		self.send_thread_ACK = threading.Thread(target=self.send_ACK_thread_util, daemon=True)
		self.send_thread.start()
		self.recv_thread.start()
		self.send_thread_ACK.start()	

	def send_at_a_time(self):
		#global send_buff
		tic = time.time()
		for i in range(100):
			self.send("Hello")
		while(len(self.send_buff)!=0):
			pass
		toc=time.time()
		total_time = toc-tic
		throughput= (self.length*8)/total_time
		print("throughput = "+str(throughput)+ " bits/sec")


	def send(self, text_msg):
		'''
		API function which takes a text message to be send.
		0 is for normal packet type
		'''
		packet = Packet(text_msg, self.seq_num_send, 0)
		self.seq_num_send += 1
		self.send_buff.append(packet)

	def recv(self):
		'''
		API function to receive a text message or -1 if no 
		message to receive.
		'''
		if (len(self.recv_buff) == 0):
			return -1
		else:
			packet = self.recv_buff[0]
			self.recv_buffer.pop(0)
			return packet.data

	def close(self):
		'''
		API function to stop all the helper threads.
		'''
		self.signal = False

	def send_thread_util(self):
		"""
		Thread that continuously keep sending message packets 
		stored in send_buff after some specified interval.
		"""
		while (self.signal):
			# Array to store index of packets to be deleted.
			del_list = []

			for ind in range( min( len(self.send_buff), self.cwnd_size) ):
				if (self.send_buff[ind].ack_rcvd == False):
					packet = self.send_buff[ind]

					# Create string to be sent over UDP packet
					# with necessary information.
					send_data = str(packet.type) + "\n" + str(packet.seq_num) + "\n" + str(packet.data) + "\n"
					self.length+=len(send_data)
					send_data = send_data.encode('utf-8')

					self.sock.sendto(send_data, self.host_addr)

				else:
					del_list.append(ind)

			#delete packets whose ACK has been recvd
			for ind in sorted(del_list, reverse=True):
				del self.send_buff[ind]

			time.sleep(1)

	def send_ACK_thread_util(self):
		'''
		Thread that continuously keep sending ACK packets
		stored in send_buff_ACK after some specified interval.
		'''
		while (self.signal):
			# Array to store index of ACK packets to be deleted.
			del_list = []

			for ind in range ( min( len(self.send_buff_ACK), self.cwnd_size) ):
				packet = self.send_buff_ACK[ind]

				# Create string to be sent over UDP packet with neccessary
				# information.
				send_data = str(packet.type) + "\n" + str(packet.seq_num) + "\n"

				send_data = send_data.encode('utf-8')

				self.sock.sendto(send_data, self.host_addr)
				del_list.append(ind)
				# delete current packet

			# Remove packets that have been marked for deletion.
			for ind in sorted(del_list, reverse=True):
				del self.send_buff_ACK[ind]

			time.sleep(1)

	def recv_thread_util(self):
		'''
		Thread that continously looks for received packets
		and take necessary action based on wether they are 
		message packets or ACK packets.
		'''
		while (self.signal):
			data, address = self.sock.recvfrom(4096)
			# check if it's correct host, maybe later
			data = data.decode('utf-8')
			print("data received\n", data)

			# Converts parameters in string form to a list.
			data = data.split('\n')

			if (int(data[0]) == 0):
				# If packet type is message packet.

				packet = Packet(data[2], int(data[1]), int(data[0]))
				if (packet.seq_num < self.seq_num_recv):
					# If packet is an old received packet re-received
					# then drop packet and resend its ACK.
					pass

				elif (packet.seq_num == self.seq_num_recv):
					# If packet has sequence number that was expected.
					self.recv_buff.append(packet)
					self.seq_num_recv += 1

				else:
					# If some future packet having sequence number greater
					# than expected is received, simply drop packet and
					# don't send and ACK for it. It will be resend by other
					# host in future.
					continue

				# Create an ACK packet for currently received packet and 
				# pass it to send_buff_ACK.
				ACK_packet = Packet("", data[1], 1)
				self.send_buff_ACK.append(ACK_packet)

			else:
				# If packet type is ACK packet, then mark ack_recvd as
				# true for corresponding packet in send_buff. It will
				# be automatically deleted from there later.
				for ind in range( len(self.send_buff) ):
					if (self.send_buff[ind].seq_num == int(data[1])):
						self.send_buff[ind].ack_rcvd = True
						break

	
	


