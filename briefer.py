import os
import nounsEngine
import adjectivesEngine
from flask import Flask, request, session, g, redirect, url_for, abort, render_template


app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()
