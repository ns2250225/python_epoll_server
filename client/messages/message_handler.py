#-*- coding:utf-8 -*-
import protocol.c2s_protocol


def handle_S2C_LOGIN(session_obj, msg_data):
	print "handle_S2C_LOGIN"
	send_msg ={}
	session_obj.send_msg(protocol.c2s_protocol.C2S_GET_ACCOUNT_INFO, send_msg)
	
	
def handle_S2C_GET_ACCOUNT_INFO(session_obj, msg_data):
	print "handle_S2C_GET_ACCOUNT_INFO"
	





