#-*- coding:utf-8 -*-
import protocol.c2s_protocol

def handle_C2S_LOGIN(session_obj, msg_dict):
	send_msg ={}
	send_msg["errcode"] = 0
	send_msg["account_id"] = 128
	
	session_obj.send_msg(protocol.c2s_protocol.S2C_LOGIN, send_msg)


def handle_C2S_GET_ACCOUNT_INFO(session_obj, msg_dict):
	send_msg ={}
	send_msg["acocunt_id"] = 123
	send_msg["nick_name"] = "test1"
	send_msg["coin"] = 3000
	
	session_obj.send_msg(protocol.c2s_protocol.S2C_GET_ACCOUNT_INFO, send_msg)
	



