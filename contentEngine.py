import RetrieveTweets
import RetrieveWiki

def genContent(keyword):
	htmlString = "<div style='width:400px;height:400px'>" + RetrieveWiki.genWikiExcerpt(keyword) + "<hr>" + RetrieveTweets.retrieveTweets(keywords) + "</div>"

	return htmlString

def newsContent(keyword):
	# Use alchemy to find relevant news articles and its semantic analysis, 
	# format into HTML
	htmlString = ""
	return htmlString