import matplotlib.pyplot as plt
import yfinance as yf
import getStockData as gsd

def getData():
    stockList= gsd.startCollectStock()

    tickers= []
    for stock in stockList:
        tickers.append(stock.ticker)
    
    return plotData(tickers)

def plotData(data):
    plotList= []

    for element in data:
        all_data= yf.Ticker(f"{element}")
        hist= all_data.history(period= "1mo", interval= "1d")
        histClose= hist["Close"]
        dates= hist.index
        
        plotList.append(createPlot(element, dates, histClose))
    
    return plotList
    
def createPlot(stock, dates, closePrice):
   
    plot= plt.figure(figsize= (10,5))
    plt.plot(dates, closePrice, marker= "o", linestyle= "-", color= "green")
    plt.title(f"{stock}")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return plot
