from TwitterSearch import *

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

        htmlstring = ""
        print "lolpls"

        i = 0
        for tweet in ts.search_tweets_iterable(tso):
            htmlstring += "<div><strong><a href='http://twitter.com/%s'>@%s</a></strong> %s" % (tweet['user']['screen_name'], tweet['user']['screen_name'], tweet['text']) + '</div>'

            i += 1
            if i > 1:
                break

    except TwitterSearchException as e:
        print(e)

    return htmlstring