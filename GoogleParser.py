from bs4 import BeautifulSoup
import operator
import urllib
import rake
from HTMLParser import HTMLParser

def pGoogle(keyword):
	response = urllib.urlopen("https://www.google.com/#safe=off&q=" + keyword)
	soup = BeautifulSoup(response, 'html.parser')
	print soup
	cat = soup.find_all("a", {"class":"fl"})
	nCat = []
	nVals = []
	val = soup.find_all("span", {"class":"kno-fv"})
	title = soup.find("span", {"class":"kno-fb-ctx"})
	gCards = []
	for c in cat:
		print "hi"
		nCat.append(''.join(c.find_all(text=True)).strip())
	for v in val:
		nVals.append(''.join(v.find_all(text=True)).strip())
	for i in range(0, len(nCat)):
		gCards.append({
			"title": title,
			"cat": nCat[i],
			"val": nVals[i]
		})
	return gCards

