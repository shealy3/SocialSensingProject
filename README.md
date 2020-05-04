Sean Healy, Nick Fahrney, Conor Rinehart

Social Sensing and Cyber-Physical Systems

Here is a quick breakdown of what is in our code repository...

sentanal.py contains the functions that carry out the sentiment analysis using TextBlob. The analyze_tweets functions take in list of tweets and perform sentiment analysis on them, which produces a total sentiment analysis score for the whole list. 

create_baseline.py is somewhat self-explanatory. This is the script that produces the baseline with the data from the stock's history to be used in later analysis of current data relative to normal performance. Sample output of this program can be seeen in the file TeslaStock.txt.

get_stock_data.py contains some of the implementation of yfinance that is used to gather data about the company's stock price over a time period.

Main.py is the main function that get relative sentiment scores for a given time period. You can generate the baseline at the same time if you want to, but it usually makes more sense to generate the baseline separately and hard-code it into the program because of how long baseline() takes to run. This file is adapted from the main function of GetOldTweets.

For best results, please run programs on the Notre Dame network via VPN if in-person access is not possible.

For more information on what is going on in our code, we recommend looking at our final paper, which is also in this directory.

For more information on how GetOldTweets works, see the file GetOldTweetsREADME.md


Link to repository: https://github.com/shealy3/SocialSensingProject
