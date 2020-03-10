import csv
with open('dataset.csv','r') as f:
	reader = csv.reader(f)
	header_row = next(reader)
	ip=[]
	tp=[]
	for row in reader:
#		print(row[0])
		ip.append(row[0])
		tp.append(row[1])
f.close()

nip=[]
ntp=[]
for i in ip:
	if i not in nip:
		nip.append(i)
		count =ip.index(i)
		ntp.append(tp[count])
	elif i in nip:
		count1 = ip.index(i)
		count2 = nip.index(i)
		if float(tp[count1]) >float(ntp[count2]):
			ntp[count2] = tp[count1]
for i in range(len(nip)):
	with open('newdataset.csv','a+') as f:
		f.write(nip[i] + ','+ ntp[i] + '\n')
