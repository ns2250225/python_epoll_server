#-*- coding:utf-8 -*-
import socket

class Listener(object):
	def __init__(self):
		self.__sock = None
		
	
	def get_sock(self):
		return self.__sock
	
	
	def __create_listener(self, port, backlog):
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__sock.setblocking(False)
		self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		server = ("0.0.0.0", port)
		self.__sock.bind(server)
		
		self.__sock.listen(backlog)
		
		
	def create(self, port, backlog):
		try:
			self.__create_listener(port, backlog)
			return True
			
		except:
			return False



