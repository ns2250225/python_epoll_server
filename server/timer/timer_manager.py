#-*- coding:utf-8 -*-
import time

class TimerManager(object):
	def __init__(self):
		self.__last_check_1s_time =0
		self.__last_check_3s_time =0
		
		
	def handle_1s_timer(self, now):
		return
	
	
	def handle_3s_timer(self, now):
		return
	
	
	
	def check_timers(self):
		now =time.time()
		if now >= self.__last_check_1s_time + 1:
			self.handle_1s_timer(now)
			self.__last_check_1s_time = now
			
		if now >= self.__last_check_3s_time + 3:
			self.handle_3s_timer(now)
			self.__last_check_3s_time = now
		



