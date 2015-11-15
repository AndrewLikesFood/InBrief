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
	htmlStrings = []

	# For each noun, generate html string
	for noun in nouns:
		htmlStrings.append(contentEngine.genContent(noun))
	for i in range(0, NUM_NEWS):
		htmlStrings.append(contentEngine.newsContent(keyword))

	# Pass html strings into resultsPage to generate graphic.
	return render_template('resultsPage.html', data=htmlStrings)


if __name__ == "__main__":
	app.run()


