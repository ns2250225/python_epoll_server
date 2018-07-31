#-*- coding:utf-8 -*-
#用一个客户端测试服务端
import network.client_session
import protocol.c2s_protocol
import time

def send_login(session_obj):
	send_msg ={}
	send_msg["account_name"] ="test"
	send_msg["password"] ="123456"
	session_obj.send_msg(protocol.c2s_protocol.C2S_LOGIN, send_msg)


def test_server():
	session_obj = network.client_session.ClientSession()
	ret = session_obj.connect("192.168.1.133", 1234)
	if ret ==False:
		return
	
	while True:
		send_login(session_obj)
		session_obj.recv_messages()
		session_obj.send_all()
		
		time.sleep(1)



