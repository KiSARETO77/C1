import aminolib,ujson,time
for a in ujson.load(open("accounts.json")):
	e,p,d,SID=a["email"],a["password"],a["device"],a["SID"]
	c = aminolib.Client(d)
	try:
		c.login(e,p)
		print(f'Logged in {e}')
		c.join_community("105025706")
		c.check_lottery("105025706")
	except Exception as e:
		print(e)
		pass
		for i in range(24):
			try:
				c.send_active("105025706")
				print(f"send time {i+1}")
				time.sleep(12)
			except Exception as e:
				print(e)
				time.sleep(20)
				pass
