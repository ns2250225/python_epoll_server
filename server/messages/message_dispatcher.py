#-*- coding:utf-8 -*-
import protocol.c2s_protocol
import messages.message_handler

class MessageDispatcher(object):
	def __init__(self):
		self.__handler_dict ={}
		self.initialize()
		
		
	def initialize(self):
		self.__handler_dict[protocol.c2s_protocol.C2S_LOGIN] = messages.message_handler.handle_C2S_LOGIN
		self.__handler_dict[protocol.c2s_protocol.C2S_GET_ACCOUNT_INFO] = messages.message_handler.handle_C2S_GET_ACCOUNT_INFO
		
		
		
	def dispatch(self, session_obj, msg_id, msg_data):
		print "MessageDispatcher:dispatch,  msg_id=%d, msg_data=%s"%(msg_id, msg_data)
		
		handler = self.__handler_dict.get(msg_id, None)
		if handler ==None:
			print "******MessageDispatcher:dispatch, fail to get handler  for msg_id=%d"%msg_id
			return
		
		handler(session_obj, msg_data)
		
