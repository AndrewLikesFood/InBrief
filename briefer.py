import os
import nounsEngine
import adjectivesEngine
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from TwitterSearch import *

app = Flask(__name__)
def retrieveTweets(keyword):
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords([keyword])
        tso.set_language('en')
        tso.set_include_entities(False)
        ts = TwitterSearch(
            consumer_key = 'dxDoYB875ZUsvgPtp8EVDkyq6',
            consumer_secret = '6v4GiG1B3zKmJOsYPEtb0b39lv9da7iu7pIdAANyIoisoNrtZY',
            access_token = '2157789854-Fwr0uDJQ23twqSyxPEH0VnPwafQvpay8K2z7aFQ',
            access_token_secret = 'q9S6ECBpBv1RMBG8iNT8cYdoJvQAoIMZfMHAivs5Fh0PQ')

        i = 0
        for tweet in ts.search_tweets_iterable(tso):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

            i += 1
            if i > 10:
                break

    except TwitterSearchException as e:
        print(e)

@app.route("/")
def search():
    retrieveTweets('Paris')
    return render_template('searchPage.html')

@app.route("/results")
def index():
	return render_template('resultsPage.html')

if __name__ == "__main__":
	app.run()


