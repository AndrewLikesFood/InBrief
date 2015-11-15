import json
import urllib

def getNewsExcerpts(keyword):
	url = "https://access.alchemyapi.com/calls/data/GetNews?apikey=42637cbfb3db625cd2d5e3482d78f04cd390bb46&return=enriched.url.title,enriched.url.url,enriched.url.enrichedTitle.entities,enriched.url.enrichedTitle.docSentiment,enriched.url.enrichedTitle.concepts,enriched.url.enrichedTitle.taxonomy&end=1447628400&start=1446940800&q.enriched.url.cleanedTitle=" + urllib.quote_plus(keyword) + "&count=25&outputMode=json"
	print url
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	htmlStrings = []
	miniTitles = []
	print "News loaded."
	endRange = 4
	for i in range(0, endRange):
		if i == len(data["result"]["docs"]):
			break
		if len(data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["concepts"]) == 0:
			i = i + 1
			endRange = endRange + 1 
			continue
		title = data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["concepts"][0]["text"]
		headline = data["result"]["docs"][i]["source"]["enriched"]["url"]["title"]
		url = data["result"]["docs"][i]["source"]["enriched"]["url"]["url"]
		sentiment = data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["docSentiment"]["score"]
		entities = ""
		for j in range(0, len(data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["entities"])):
			entities = entities + (data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["entities"][j]["text"]) + ", "
		if(data["result"]["docs"][i]["source"]["enriched"]["url"]["enrichedTitle"]["entities"]) > 0:
			entities = entities[:(len(entities) - 2)]
		miniTitles.append(title)
		htmlStrings.append("<div style='width:100%'><strong>" + headline + "</strong><br><b>Sentiment:</b>" + str(sentiment)  + "<br><b>Entities:</b> " + entities + "<br><a href='" + url + "'>Read more</a></div>")
	return {
		"strings": htmlStrings,
		"titles" : miniTitles
	}
	return "NEWS"