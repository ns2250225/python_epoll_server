#-*- coding:utf-8 -*-
import select

class IOEvent(object):
	def __init__(self):
		self.__epoll_object = select.epoll()
		
	#等待epoll事件
	def wait_events(self, timeout_ms):
		event_list = self.__epoll_object.poll(timeout_ms)
		return event_list
	
	
	#给sockfd注册一个epoll事件
	def register_events(self, sockfd, events):
		self.__epoll_object.register(sockfd, events)
		
	
	#修改sockfd的epoll事件
	def update_events(self, sockfd, events):
		self.__epoll_object.modify(sockfd, events)
		
	
	#删除sockfd的epoll事件
	def remove_event(self, sockfd):
		self.__epoll_object.unregister(sockfd)
		

