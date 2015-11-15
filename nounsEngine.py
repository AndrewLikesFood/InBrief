import json
import rake
import operator
import urllib

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def stripBlacklist(listFile, tuples):
	blist = open(listFile, "r").read().split('\n')
	return [i for i in tuples if i[0] not in blist ]

def retrieveTopNouns(keyword):
	url = "https://en.wikipedia.org/w/api.php?action=parse&redirects&prop=text&format=json&page=" + urllib.quote_plus(keyword)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	rake_object = rake.Rake("SmartStoplist.txt", 5, 3, 4)
	keywords = rake_object.run(strip_tags(data['parse']['text']['*']))
	keywords = stripBlacklist("blackList.txt", keywords)
	return [wd[0] for wd in keywords[:6]]