import os
import nounsEngine
import adjectivesEngine
import contentEngine

from flask import Flask, request, session, g, redirect, url_for, abort, render_template

NUM_NEWS = 4
app = Flask(__name__)

@app.route("/")
def search():
    return render_template('searchPage.html')

@app.route("/<keyword>")
def ruckme(keyword):
	# Fetch nouns associated with keyword
	nouns = nounsEngine.retrieveTopNouns(keyword)
	miniTitles = []
	htmlStrings = []

	# For each noun, generate html string
	for noun in nouns:
		miniTitles.append(noun)
		htmlStrings.append(contentEngine.genContent(noun))
	
	print "Content actually done."
	newsList = contentEngine.newsContents(keyword)
	for i in range(0, len(newsList['strings'])):
		print newsList
		htmlStrings.append(newsList['strings'][i])
		miniTitles.append(newsList['titles'][i])

	print "News done"
	# Pass html strings into resultsPage to generate graphic.
	print htmlStrings
	print miniTitles
	return render_template('resultsPage.html', htmlStrings=htmlStrings, miniTitles=miniTitles)


if __name__ == "__main__":
	app.run()


