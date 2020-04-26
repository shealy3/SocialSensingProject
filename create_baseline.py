import sys
import io
from sentanal import analyze_tweets
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
import yfinance as yf
from datetime import timedelta

def check_stats(TimeStart, TimeEnd, content):
    start = TimeStart.strftime("%Y-%m-%d")
    end = TimeEnd.strftime("%Y-%m-%d")
    #print(start, end)
    #gather tweets from this time
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(content).setSince(start).setUntil(end).setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    #get the data scores from this time and return
    return analyze_tweets(tweets)


def compare_nums(score, stocks, startStock):
    if stocks/startStock < .15 and stocks/startStock > -.1:
        print(score)
        return score

def correlation(correlations, base):
    true = 0
    for i in correlations:
        if i[1] > 0 and (i[0] - base) > 0:
            true += 1
    return true / len(correlations) * 100

def baseline(content="tesla", stock="TSLA"):
    correlationStats = []
    stockdata = yf.Ticker(stock)
    hist = stockdata.history(period="10mo")

    counter = 0
    databytime = []
    totalWeek = 0
    done = True
    while counter < len(hist):
        if counter % 21 == 1 and done is False:
            end = hist.index[counter-1]
            score = check_stats(start-timedelta(7), end, content)
            if compare_nums(score, totalWeek, startStock):
                databytime.append(compare_nums(score, totalWeek, startStock))
            correlationStats.append([score, totalWeek])
            done = True
        if counter % 21 == 1 and done is True:
            totalWeek = 0
            start = hist.index[counter]
            startStock = hist["Open"][counter]
            done = False
        totalWeek += hist["Close"][counter] - hist["Open"][counter]
        counter += 1
    base = sum(databytime) / len(databytime)
    corr = correlation(correlationStats, base)
    fileName = "tesla.txt"
    with io.open(fileName, "a", encoding="utf-8") as f:
        for i in correlationStats:
            f.write(str(i[1]) + " " + str(i[0]-base))
            f.write("\n")
        f.write("\n")
        f.write("Base: " + str(base))
        f.write("\n")
        f.write("Correlation: " + str(corr))
    return base

baseline()

