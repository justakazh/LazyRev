import requests
import json
from multiprocessing.dummy import Pool
print("""

  _                     _____            
 | |                   |  __ \           
 | |     __ _ _____   _| |__) |_____   __
 | |    / _` |_  / | | |  _  // _ \ \ / /
 | |___| (_| |/ /| |_| | | \ \  __/\ V / 
 |______\__,_/___|\__, |_|  \_\___| \_/  
                   __/ |                 
                  |___/   -gabut version-               

*Gausah ngeluh result dikit, bikin bot sendiri kalo mau banyak\n*Tetap prangas prenges senajan result gawe stress"
Coded by @justakazh
---------------------------------------------------------------------------
	""")
open("ips.txt", "a")

def LazyRev(url):
	try:
		site = url.replace("https://","").replace("http://","").replace("/","").strip()
		r = requests.get("https://justakazh.nasihosting.com/api/?url="+site).content
		de = json.loads(r)
		for i in de:
			try:
				print("[>] http://"+i)
				open("_LazyRev.txt", "a").write("http://"+i+"\n")
			except:
				pass
	except:
		pass

lismu = [i.strip() for i in open(raw_input("List > "), "r").readlines()]
z = Pool(input("Thread > "))
z.map(LazyRev, lismu)