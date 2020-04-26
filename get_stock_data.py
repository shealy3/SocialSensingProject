import yfinance as yf
import pandas as pd


def get_stocks():
    #define the ticker symbol
    msft = yf.Ticker("TSLA")
    hist = msft.history(period="100mo")
    '''tickerSymbol = 'MSFT'

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')'''

    #see your data
    databymonth = []
    counter = 1
    count = 0
    print(hist["Open"][0])
    databymonth.append(0)
    for i in hist["Close"]:
        if counter > 30:
            counter = 1
            count += 1
            databymonth.append(i)
        else:
            databymonth[count] += i
        counter += 1
        #print(i)
    counter = 1
    count = 0
    for i in hist["Open"]:
        if counter > 30:
            counter = 1
            count += 1
        databymonth[count] -= i
        counter += 1

    '''for i in databymonth:
        print(i)
    print(len(databymonth))'''
get_stocks()