import shutil
a = 0
readDir = 'F:\\UCL\\python\\urls.txt'
writeDir = 'F:\\UCL\\python\\NEWURL.txt'
lines_seen = set()
outfile = open(writeDir, "w")
f = open(readDir, "r")
for line in f:
	if line not in lines_seen:
		a+=1
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
print("success")