#-*- coding:utf-8 -*-
import network.buffer
import socket, errno

class SessionBase(object):
	def __init__(self):
		self.send_buff = network.buffer.Buffer()
		self.recv_buff = network.buffer.Buffer()
		self.__sock = None
		self.__connected = False
		self.__last_recv_time = 0 #最近接收消息的时间
		self.__connecting =False
		
		
	def initialize(self):
		self.send_buff.clear_data()
		self.recv_buff.clear_data()
		self.__sock = None
		self.__connected =False
		self.__last_recv_time =0
		self.__connecting =False
		
	def release(self):
		if self.__sock <>None:
			self.__sock.close()
			
		self.__sock = None
		self.send_buff.clear_data()
		self.recv_buff.clear_data()
		self.__connected =False
	
	def close(self):
		self.release()
		
	def get_sock(self):
		return self.__sock
	
	def is_connected(self):
		return self.__connected
	
	def set_connected(self, connected):
		self.__connected = connected
		
	
	def set_last_recv_time(self, now):
		self.__last_recv_time =  now
		
	def get_last_recv_time(self):
		return self.__last_recv_time
	
	
	def set_blocking(self, blocking):
		if self.__sock <>None:
			self.__sock.setblocking(blocking)
			
	#连接服务端
	def connect(self, host, port):
		if self.__sock == None:
			self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
		print "----------try to connect host=%s, port=%d"%(host, port)
		try:
			self.__sock.settimeout(5)
			self.__sock.connect((host, port))
			
		except socket.error:
			print "********fail to connect to host %s, port %d"%(host, port)
			self.__connecting = False
			return False
		
		print "--------->connected to host, port", host, port
		self.set_blocking(False)
		self.__connected = True
		self.__connecting = False
		return True	
			
	
	def recv_all(self):
		if self.__sock == None:
			return
		
		while True:
			try:
				data = self.__sock.recv(4096)
				if len(data) >0:
					self.recv_buff.push(data)
					
				elif len(data) ==0:
					print "----------recv_all: connection closed"
					self.__connected =False
					return
				
			except:
				return
				
				
	def send_all(self):
		if self.__sock ==None:
			return
		
		while True:
			try:
				data = self.send_buff.peek(4096)
				if data == None:
					return
				
				data_len = self.__sock.send(data)
				if data_len >0:
					self.send_buff.update_offset(data_len)
					#print "send_all: data_len=",data_len
					
				else:
					return
					
			except:
				return
	

