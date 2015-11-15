import json
import urllib

def getWikiExcerpt(keyword):
	url = "https://en.wikipedia.org/w/api.php?format=json&redirect&action=query&prop=extracts&exintro=&explaintext=&titles=" + urllib.quote_plus(keyword)
	print url
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	if data['query']['pages'].keys()[0] == "-1":
		return "<div style='width:100%'><strong>Wikipedia</strong></div>"
	title = data['query']['pages'].itervalues().next()['title']
	data = data['query']['pages'].itervalues().next()['extract']
	iterBegin = 200 if len(data) > 200 else len(data)
	iterEnd = 300 if len(data) > 300 else len(data)
	if iterBegin == 200:
		for i in range(iterBegin, iterEnd - 1):
			if data[i] == "." and (data[i + 1] == "\n" or data[i + 1] == " "):
				data = data[:(i + 1)]
				break
			if i == iterEnd - 2:
				data = data[:i] + ". . ."

	return data

