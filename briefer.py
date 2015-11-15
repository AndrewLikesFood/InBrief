import os
import json
import nounsEngine
import adjectivesEngine
import contentEngine
import unicodedata
import urllib

from flask import Flask, request, session, g, redirect, url_for, abort, render_template

NUM_NEWS = 4
app = Flask(__name__)

@app.route("/")
def search():
    return render_template('searchPage.html')

@app.route("/<keyword>")
def ruckme(keyword):
	# Fetch nouns associated with keyword
	# print "below are the nouns"
	#keyword = unicodedata.normalize("NFKD", keyword).encode("ascii", "ignore")
	nouns = nounsEngine.retrieveTopNouns(keyword)
	# print nouns
	miniTitles = []
	htmlStrings = []
	# For each noun, generate html string
	for noun in nouns:
		print noun
		miniTitles.append(noun)
		htmlStrings.append(contentEngine.genContent(noun))
	
	print "Content actually done."
	newsList = contentEngine.newsContents(keyword)
	for i in range(0, len(newsList['strings'])):
	 	print newsList
	 	htmlStrings.append(newsList['strings'][i])
	 	miniTitles.append(newsList['titles'][i])

	# print "News done"
	# Pass html strings into resultsPage to generate graphic.

	# print htmlStrings
	# print miniTitles
	url = "http://jss.party/json/" + keyword + "Card.json"
	print url
	response = urllib.urlopen(url)
	cardData = json.loads(response.read())
	return render_template('resultsPage.html', htmlStrings=htmlStrings, miniTitles=miniTitles, cardData=cardData)

if __name__ == "__main__":
	app.run()


