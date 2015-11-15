import RetrieveTweets
import RetrieveWiki
import RetrieveNews
import twitterParser

def genContent(keyword):
	print "content"
	tweets = twitterParser.parseTwitter(keyword)
	htmlString = "<div class=\"titlePanel\">" + keyword + "</div> <i id=\"twitterIcon\" style=\"font-size: 35px\" class=\"fa fa-twitter\"></i><div class=\"twitterPanel\">" + tweets[0]["tweet"] + "</div> <i id="wikipediaIcon" style=\"font-size: 30px;\" class='fa fa-wikipedia-w'></i> <a href=\"https://en.wikipedia.org/wiki/" + keyword + "\" class=\"wikipediaPanel\">" + RetrieveWiki.getWikiExcerpt(keyword) + "</a>"
	return htmlString

def newsContents(keyword):
	# Use alchemy to find relevant news articles and its semantic analysis, 
	# format into HTML
	return RetrieveNews.getNewsExcerpts(keyword)