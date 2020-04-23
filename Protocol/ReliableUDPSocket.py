import socket
import threading
import time

class Packet:
	ack_rcvd = False
	seq_num = 0
	data = ""
	type = 0
	#type 0 is for data packet, 1 is for ACK packet

	def __init__(self, data, seq_num, type):
		self.data = data
		self.seq_num = seq_num
		self.type = type

class ReliableUDPSocket:
	send_buff = []
	send_buff_ACK = []
	recv_buff = []

	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	seq_num_send = 0
	seq_num_recv = 0
	cwnd_size = 10
	
	IP_addr = "0.0.0.0"
	port = 50000

	def __init__(self, src_IP, src_port, dest_IP, dest_port):
		self.src_IP= src_IP
		self.src_port = src_port
		self.sock.bind((self.src_IP, self.src_port))
		self.host_addr = (dest_IP, dest_port)
		self.signal = True
		print("socket created", self.sock)

		self.send_thread = threading.Thread(target=self.send_thread_util, daemon=True)
		self.recv_thread = threading.Thread(target=self.recv_thread_util, daemon=True)
		self.send_thread_ACK = threading.Thread(target=self.send_ACK_thread_util, daemon=True)
		self.send_thread.start()
		self.recv_thread.start()
		self.send_thread_ACK.start()	

	def send(self, text_msg):
		#0 is for normal packet type
		packet = Packet(text_msg, self.seq_num_send, 0)
		self.seq_num_send += 1
		self.send_buff.append(packet)

	def recv(self):
		if (len(self.recv_buff) == 0):
			return -1
		else:
			packet = self.recv_buff[0]
			self.recv_buffer.pop(0)
			return packet.data

	def close(self):
		self.signal = False

	def send_thread_util(self):
		while (self.signal):
			del_list = []

			for ind in range( min( len(self.send_buff), self.cwnd_size) ):
				if (self.send_buff[ind].ack_rcvd == False):
					packet = self.send_buff[ind]
					send_data = str(packet.type) + "\n" + str(packet.seq_num) + "\n" + str(packet.data) + "\n"
					send_data = send_data.encode('utf-8')
					self.sock.sendto(send_data, self.host_addr)
				else:
					del_list.append(ind)

			#delete packets whose ACK has been recvd
			for ind in sorted(del_list, reverse=True):
				del self.send_buff[ind]

			time.sleep(1)

	def send_ACK_thread_util(self):
		while (self.signal):
			del_list = []

			for ind in range ( min( len(self.send_buff_ACK), self.cwnd_size) ):
				packet = self.send_buff_ACK[ind]
				send_data = str(packet.type) + "\n" + str(packet.seq_num) + "\n"
				send_data = send_data.encode('utf-8')
				self.sock.sendto(send_data, self.host_addr)
				del_list.append(ind)
				# delete current packet

			for ind in sorted(del_list, reverse=True):
				del self.send_buff_ACK[ind]

			time.sleep(1)

	def recv_thread_util(self):
		while (self.signal):
			data, address = self.sock.recvfrom(4096)
			# check if it's correct host, maybe later
			data = data.decode('utf-8')
			print("data received\n", data)
			data = data.split('\n')

			if (int(data[0]) == 0):
				packet = Packet(data[2], int(data[1]), int(data[0]))
				if (packet.seq_num < self.seq_num_recv):
					#drop packet
					pass

				elif (packet.seq_num == self.seq_num_recv):
					self.recv_buff.append(packet)
					self.seq_num_recv += 1

				else:
					#drop packet and don't send ACK
					continue

				ACK_packet = Packet("", data[1], 1)
				self.send_buff_ACK.append(ACK_packet)

			else:
				for ind in range( len(self.send_buff) ):
					if (self.send_buff[ind].seq_num == int(data[1])):
						self.send_buff[ind].ack_rcvd = True
						break

