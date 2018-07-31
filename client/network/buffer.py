#-*- coding:utf-8 -*-

class Buffer(object):
	def __init__(self):
		self.__data = ''
		
	#将数据添加到缓存的后面
	def push(self, data):
		self.__data += data
	
	
	#从缓存中提取长度为data_len的数据,将提取的数据从缓存中删除
	def pop(self, data_len):
		if len(self.__data) < data_len:
			return
		
		data = self.__data[:data_len]
		self.__data = self.__data[data_len:]
		return data
	
	
	#从缓存中查看数据长度为data_len的数据,不会将数据从缓存中删除
	def peek(self, data_len):
		if len(self.__data) ==0:
			return None
		
		if len(self.__data) < data_len:
			data_len = len(self.__data)
			
		data = self.__data[:data_len]
		return data
	
	#更新缓存的数据偏移，将数据从缓存的前删除
	def update_offset(self, data_len):
		if len(self.__data) < data_len:
			self.__data = ''
			
		else:
			self.__data = self.__data[data_len:]
			
			
	def get_data_len(self):
		return len(self.__data)
	
	
	def clear_data(self):
		self.__data = ''
		
		
