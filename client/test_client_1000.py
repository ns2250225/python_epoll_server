#-*- coding:utf-8 -*-
#用1000个客户端测试服务端
import network.client_session
import protocol.c2s_protocol
import time

def send_login(session_obj):
	send_msg ={}
	send_msg["account_name"] ="test"
	send_msg["password"] ="123456"
	session_obj.send_msg(protocol.c2s_protocol.C2S_LOGIN, send_msg)


def test_server():
	session_list = []
	for i in xrange(0,1000):
		session_obj = network.client_session.ClientSession()
		ret = session_obj.connect("192.168.1.133", 1234)
		if ret ==False:
			print "*********fail to connect server****************"
			break
		
		session_list.append(session_obj)
	
	#1000个连接, 每个连接每秒向服务端发送100个请求	
	while True:
		for session_obj in session_list:
			send_login(session_obj)
			session_obj.recv_messages()
			session_obj.send_all()
		
		time.sleep(0.01)
	


