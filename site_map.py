from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

#import urllib
import re
 
def getLinks(url):
    html_page = uReq(url)
    soup = BeautifulSoup(html_page)
    links = []
 
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))
 
    return links
links=[] 
links=getLinks("https://wiprodigital.com")

#print(links)

with open('site_map.txt', 'w') as f:
	for x in links:
		if re.match("https://wiprodigital.com", x) is not None:
			print(x,file=f)
  	



