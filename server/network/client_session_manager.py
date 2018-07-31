#-*- coding:utf-8 -*-
import network.client_session
import network.ioevent
import network.listener
import socket
import select

class ClientSessionManager(object):
	def __init__(self):
		self.__session_dict = {} #<sockfd, session>
		self.__listener = network.listener.Listener()
		self.__ioevent = network.ioevent.IOEvent()
		
	
	def initialize(self):
		return
	
	def release(self):
		return
	
	
	def get_listener_object(self):
		return self.__listener
	
	def get_ioevent_object(self):
		return self.__ioevent
	
	
	#添加一个session对象
	def add_session(self, session_obj):
		sock = session_obj.get_sock()
		self.__session_dict[sock.fileno()] = session_obj
		self.__ioevent.register_events(sock.fileno(), select.EPOLLIN | select.EPOLLET)
	
	#创建一个session对象
	def create_session(self, sock):
		session_obj = network.client_session.ClientSession(sock)
		self.add_session(session_obj)
		return session_obj
	
	#删除一个session对象
	def drop_session(self, session_obj):
		sock = session_obj.get_sock()
		if self.__session_dict.has_key(sock.fileno()):
			self.__session_dict.pop(sock.fileno())
			
		self.__ioevent.remove_event(sock.fileno())
		session_obj.release()
			
	def get_session(self, sockfd):
		return self.__session_dict.get(sockfd, None)
	
	#接受所有连接
	def accept_all_connections(self, listener_sock):
		while  True:
			try:
				new_conn = listener_sock.accept()
				if new_conn ==None:
					return
				
				sock, addr = new_conn
				print "accept_all_connections: sockfd=%s, addr=%s"%(sock.fileno(), addr)
				new_session_obj = self.create_session(sock)
				new_session_obj.set_connected(True)
				new_session_obj.set_blocking(False)
				
			except:
				return
	
	#处理所有io事件
	def handle_io_event(self):
		listener_sock = self.__listener.get_sock()
		drop_session_list =[]
		
		event_list = None
		try:
			event_list =self.__ioevent.wait_events(0.03)
		except:
			return
		
		for sockfd, events in event_list:
			if sockfd == listener_sock.fileno() and events & select.EPOLLIN:
				self.accept_all_connections(listener_sock)
				self.__ioevent.update_events(sockfd, select.EPOLLIN)
				
			elif events & select.EPOLLIN:
				session_obj = self.get_session(sockfd)
				session_obj.recv_messages()
				
				if session_obj.is_connected() ==False:
					drop_session_list.append(session_obj)
					
				else:
					self.__ioevent.update_events(sockfd, select.EPOLLIN | select.EPOLLET)
		
		for session_obj in drop_session_list:
			self.drop_session(session_obj)
			
	#发送全部消息
	def send_all(self):
		for session_obj in self.__session_dict.itervalues():
			session_obj.send_all()
		


