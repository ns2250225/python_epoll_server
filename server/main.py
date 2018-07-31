#-*- coding:utf-8 -*-
import messages
import network
import timer
import signal
import config
import json
import select

g_exit =False

def server_init():
	signal.signal(signal.SIGINT, handle_sigint)
	signal.signal(signal.SIGHUP, signal.SIG_IGN)
	
	fp = open("./config.json")
	config_data = fp.read()
	fp.close()
	
	config_dict = json.loads(config_data)
	config.LISTEN_PORT = config_dict["listen_port"]
	config.MAX_CONNECTION_COUNT = config_dict["max_connection_count"]
	
	listener_obj = network.session_manager.get_listener_object()
	ret = listener_obj.create(config.LISTEN_PORT, 100)
	if ret ==False:
		print "*******fail to create listener, port=",config.LISTEN_PORT
		return False
	
	listener_sock = listener_obj.get_sock()
	ioevent_obj =  network.session_manager.get_ioevent_object()
	ioevent_obj.register_events(listener_sock.fileno(), select.EPOLLIN)
	
	print "--------server start"
	return True


def server_exit():
	return

def handle_sigint(signo, frame):
	print "------------handle_sigint"
	global  g_exit
	g_exit =True


def server_main():
	global g_exit
	ret = server_init()
	if ret == False:
		print "******server_main: fail to init server"
		return
	
	while True:
		network.session_manager.handle_io_event()
		timer.manager.check_timers()
		network.session_manager.send_all()
		
		if g_exit:
			break
		
	server_exit()


if __name__ =="__main__":
	server_main()
	
	