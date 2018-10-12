from setting import r

get_data = r.pubsub()
get_data.subscribe("read get data")
while True:
	print("inside whoil;e")
	for data in get_data.listen():
		print("data")
	print( "listen %s" % (data['data']))