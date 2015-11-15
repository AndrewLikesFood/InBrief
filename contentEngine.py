import RetrieveTweets
import RetrieveWiki
import RetrieveNews
import twitterParser

def genContent(keyword):
	print "content"
	tweets = twitterParser.parseTwitter(keyword)
	htmlString = "<div style='display: flex; padding: 5px; justify-content: center; font-family: \"Source Sans Pro\", sans-serif; text-align: center; font-size: 30px; font-weight: bold; color: white; align-items: center; position: fixed; width: 315px; top: 240px; left: 565px; background: transparent; z-index: 100;'>" + keyword + "</div><i style='font-size: 35px;color: white;font-size: : 30px;position: fixed;top: 324px;left: 545px;z-index: 100;'class='fa fa-twitter'></i><div style='display: flex;padding: 5px;justify-content: center;font-family: \"Source Sans Pro\", sans-serif;text-align: center;color: white;align-items: center;width: 305px;height: 70px;position: fixed;top: 300px;left: 590px;background: transparent;border: 1px solid white;border-radius: 30px;z-index: 100;'>" + tweets[0]["tweet"] + "</div><i style='font-size: 30px;color: white;position: fixed;top: 445px;left: 875px;z-index: 100;'class='fa fa-wikipedia-w'></i><div style='display: flex;padding: 5px;justify-content: center;font-family: \"Source Sans Pro\", sans-serif;text-align: center;font-size: 13px;color: white;align-items: center;width: 305px;height: 160px;position: fixed;top: 390px;left: 550px;background: transparent;border: 1px solid white;border-radius: 40px;z-index: 100;'>" + RetrieveWiki.getWikiExcerpt(keyword) + "</div>"
	return htmlString

def newsContents(keyword):
	# Use alchemy to find relevant news articles and its semantic analysis, 
	# format into HTML
	return RetrieveNews.getNewsExcerpts(keyword)