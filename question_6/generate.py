from setting import r
import time
import random

while True:
	data = random.random()
	print( "sent %s" %(rand_value))
	r.publish("get data", data)