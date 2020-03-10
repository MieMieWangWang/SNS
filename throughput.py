import requests
import time
 
with open('NEWURL.txt','r') as f:
	url = f.readlines()
for i in range(len(url)):
	url[i] = url[i].strip()

	try:
		t1 = time.time()
		r = requests.get(url[i])
		t2 = time.time()
		Time = t2 - t1
		print(Time)
		print(len(r.content))
		Throughput = (len(r.content)/ (Time))
		print(Throughput)
		print(type(Throughput))
		#f = open('F:\\UCL\\python\\throughput.txt', 'a+')
	except Exception as e:
		print(e)




