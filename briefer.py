import os
import nounsEngine
import adjectivesEngine
from flask import Flask, request, session, g, redirect, url_for, abort, render_template


app = Flask(__name__)

@app.route("/")
def search():
	return render_template('searchPage.html')

@app.route("/results", methods=["POST"])
def results():
	print request.data

	return render_template('resultsPage.html', data=request.data)

if __name__ == "__main__":
	app.run()
