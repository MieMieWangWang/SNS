from urllib.parse import urlparse
import time
import socket
import requests

with open('NEWURL.txt','r') as f:
	url = f.readlines()
#print(url)
for i in range(len(url))[2501:2779]:
	url[i] = url[i].strip()
	parse_result = urlparse(url[i])
	#print(parse_result.netloc)
	try:
		IP = socket.gethostbyname(parse_result.netloc)
		print(IP)
		t1 = time.time()
		r = requests.get(url[i],timeout = 60)
		if r.status_code == 200:
			t2 = time.time()
			Time = t2 - t1
			Throughput = (len(r.content)/(Time))
			print(Throughput)
			with open ("dataset.csv","a+") as f:
				f.write(IP+','+str(Throughput)+'\n')
	except Exception as e:
		print(e)




		#f = open('F:\\UCL\\python\\throughput.txt', 'a+')
