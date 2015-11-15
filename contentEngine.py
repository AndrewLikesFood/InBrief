import RetrieveTweets
import RetrieveWiki
import RetrieveNews

def genContent(keyword):
	print "content"
	htmlString = "<div style='width:400px;height:400px'>" + RetrieveWiki.getWikiExcerpt(keyword) + "<hr></div>"# + RetrieveTweets.retrieveTweets(keyword) + "</div>"
	return htmlString

def newsContents(keyword):
	# Use alchemy to find relevant news articles and its semantic analysis, 
	# format into HTML
	return RetrieveNews.getNewsExcerpts(keyword)