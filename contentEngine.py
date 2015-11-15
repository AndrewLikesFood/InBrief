import RetrieveTweets
import RetrieveWiki

def genContent(keyword):
	htmlString = "<div style='width:400px;height:400px'>" + RetrieveWiki.getWikiExcerpt(keyword) + "<hr>" + RetrieveTweets.retrieveTweets(keyword) + "</div>"

	return htmlString

def newsContent(keyword):
	# Use alchemy to find relevant news articles and its semantic analysis, 
	# format into HTML
	htmlString = ""
	return htmlString