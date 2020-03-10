from bs4 import BeautifulSoup
import re
pageindex = 115

with open('web%d.html'%pageindex,'r') as f:
	page = f.read()
# print(page)

soup = BeautifulSoup(page, features = 'lxml')
# print(soup)
url = soup.find_all('a', href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
# print(url)
for link in url:
	# print("start")
	# str = link
	print(link)
	link = str(link)
	pattern = re.compile(r'(https?://.+?)&amp')
	res = pattern.findall(link)
	print('res=', res)
	with open('urls.txt','a+') as f:
		f.write(res[0])
		f.write('\n')

pageindex += 1