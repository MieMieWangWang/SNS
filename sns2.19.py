from bs4 import BeautifulSoup
import re
import requests
import csv
import shutil
country_website = []
final = []
website = "https://www.google.com/search?q=filetype:pdf+site:"
start = "&start="
with open("country_code.csv","r",encoding='utf8') as csvfile:
	read = csv.DictReader(csvfile)
	col = [column['Code'] for column in read]
#print(col)
	page_num=['10','20']

for v in col:
	country_url = website + v + start
	country_website.append(country_url)

html_num = 626
for i in country_website[75:77]:
	for n in page_num:
		final_url = i + n
		final.append(final_url)
		url = requests.get(final_url)
		html = url.text.encode('utf8')
		with open('web%d.html'%html_num, 'wb') as f:
			f.write(html)
		html_num+=1
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
		soup = BeautifulSoup(url.content, features = 'lxml')
# print(soup)
		url = soup.find_all('a', href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
##print(url)
		for link in url:
			#print("start")
			#str = link
			print(link)
			link = str(link)
			pattern = re.compile(r'(https?://.+?)&amp')
			res = pattern.findall(link)
			print('res=',res)
			f = open('F:\\UCL\\python\\urls.txt', 'a+')
			try:
				for i in res:
					f.write(i)
					f.write('\n')

			except:
				print('error')



