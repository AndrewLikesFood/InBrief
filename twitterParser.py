from bs4 import BeautifulSoup
import operator
import urllib
import rake
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

def parseTwitter(keyword):
	response = urllib.urlopen("https://twitter.com/search?q=" + keyword + "&src=typd&count=100")
	soup = BeautifulSoup(response, 'html.parser')
	twits = soup.find_all("p", {"class":"TweetTextSize"})
	names = soup.find_all("strong", {"class":"fullname"})
	twitTexts = []
	posters = []
	tweets = []
	raker = ""
	for node in twits:
		twitTexts.append(''.join(node.find_all(text=True)).strip())
	for name in names:
		posters.append(''.join(name.find_all(text=True)).strip().replace("\nVerified account", ""))
	for i in range(0, len(twits)):
		tweets.append({
			"name": posters[i],
			"tweet": twitTexts[i]
		})
	return tweets
