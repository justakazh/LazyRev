import requests
import json
import socket
from multiprocessing.dummy import Pool
print("""
  _                     _____            
 | |                   |  __ \           
 | |     __ _ _____   _| |__) |_____   __
 | |    / _` |_  / | | |  _  // _ \ \ / /
 | |___| (_| |/ /| |_| | | \ \  __/\ V / 
 |______\__,_/___|\__, |_|  \_\___| \_/  
                   __/ |                 
                  |___/   

Coded by @justakazh
https://github.com/justakazh
---------------------------------------------------------------------------
	""")
open("ips.txt", "a")

def LazyRev(url):
	try:
		site = url.replace("https://","").replace("http://","").replace("/","").strip()
		s = socket.gethostbyname(site)
		if s+"\n" not in open("ips.txt", "r").readlines():
			try:
				r = requests.post("http://apapedulimu.ddns.net/revip/", data={"domain":site}).text
				de = json.loads(r)
				for i in de['url']:
					print("[>] http://"+i)
					open("_LazyRev.txt", "a").write("http://"+i+"\n")
				open("ips.txt", "a").write(s+"\n")
			except:
				pass
		else:
			print(url+" | duplicate ip!")
	except:
		pass
lismu = [i.strip() for i in open(raw_input("List > "), "r").readlines()]
z = Pool(input("Thread > "))
z.map(LazyRev, lismu)
