import sys
import io
from sentanal import analyze_tweets_print
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
from create_baseline import *

def main():

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Example 1 - Get tweets by username
	'''tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)'''

	# Example 2 - Get tweets by query search
	#tweetCriteria = got.manager.TweetCriteria().setQuerySearch('tesla').setSince("2010-01-01").setUntil("2020-03-24").setMaxTweets(10)
	#tweets = got.manager.TweetManager.getTweets(tweetCriteria)
	#check_stats("2010-01-01", "2020-03-24", 'tesla')
	#analyze_tweets(tweets)
	'''fileName = "test6.txt"
	#print(tweets[0].text)
	with io.open(fileName, "a", encoding="utf-8") as f:
		for tweet in tweets:
			f.write(tweet.text)
			f.write('\n\n')'''
	base = baseline() * 10

	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('tesla').setSince("2019-05-05").setUntil("2019-05-30").setMaxTweets(100)
	tweets = got.manager.TweetManager.getTweets(tweetCriteria)

	analyze_tweets_print(tweets, base)
	'''fileName = "test.txt"
	with io.open(fileName, "a", encoding="utf-8") as f:
		for tweet in tweets:
			f.write(tweet.text)
			f.write('\n\n')'''
	#printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

	# Example 3 - Get tweets by username and bound dates
	'''tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)'''

if __name__ == '__main__':
	main()
