import aminolib,ujson,time
for a in ujson.load(open("accounts.json")):
		e,p,d,SID=a["email"],a["password"],a["device"],a["SID"]
		c = aminolib.Client(d)
		c.login(e,p)
		print(f'Logged in {e}')
		c.join_community("105025706")
		for i in range(24):
			try:
				c.send_active("105025706")
				print(f"send time {i+1}")
				time.sleep(12)
			except Exception as e:
				time.sleep(20)
				print(e)
				pass
