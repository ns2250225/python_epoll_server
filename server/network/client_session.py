#-*- coding:utf-8 -*-
import network.session_base
import json
import struct
import time
import messages

class ClientSession(network.session_base.SessionBase):
	def __init__(self, sock):
		super(ClientSession, self).__init__(sock)
		
		
	def initialize(self):
		return
	
	
	def release(self):
		super(ClientSession, self).release()
		
	#发送一个消息
	def send_msg(self, msg_id, msg_data):
		msg_dict = {}
		msg_dict["msg_id"] = msg_id
		msg_dict["msg_data"] = msg_data
		
		msg_str = json.dumps(msg_dict)
		msg_str_len = len(msg_str)
		
		msg = struct.pack("i", msg_str_len)
		msg += struct.pack(str(msg_str_len)+"s", msg_str)
		
		self.send_buff.push(msg)
		
	
	#从接收缓存取出一个数据包
	def get_next_msg(self):
		msg_header = self.recv_buff.peek(4)
		if msg_header ==None or len(msg_header) <>4:
			return None
		
		msg_str_len, = struct.unpack("i", msg_header)
		msg_len = 4 + msg_str_len
		
		if self.recv_buff.get_data_len() < msg_len:
			return None
		
		msg = self.recv_buff.pop(msg_len)
		msg_str, = struct.unpack(str(msg_str_len)+"s", msg[4:])
		return msg_str
	
	#接收和处理所有消息
	def recv_messages(self):
		now = time.time()
		self.recv_all()
		
		msg_count =0
		while True:
			msg_str = self.get_next_msg()
			if msg_str ==None:
				return
			
			#处理一个消息
			msg_data_dict = json.loads(msg_str)
			msg_id = msg_data_dict["msg_id"]
			msg_data = msg_data_dict["msg_data"]
			messages.dispatcher.dispatch(self, msg_id, msg_data)
			
			self.set_last_recv_time(now)
			
			msg_count += 1
			if msg_count > 10:
				return
			


