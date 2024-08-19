from yahooquery import Screener
from storeUnit import stockUnit

def startCollectStock():
    stockData= Screener()
    collectedData= stockData.get_screeners("most_actives", count= 25)
    collectStockData(collectedData)
    
def collectStockData(data):
    most_actives = data.get("most_actives", {})
    stockQuotes= most_actives.get("quotes", [])
    stockList= []
    
    for stock in stockQuotes:
        stockId = stock.get("longName", "N/A")
        ticker = stock.get("symbol", "N/A")
        currentPrice = stock.get("postMarketPrice", 0.0)
        openPrice = stock.get("regularMarketOpen", 0.0)
        closePrice = stock.get("postMarketPrice", 0.0)
        change = stock.get("postMarketChangePercent", 0.0)
        mCap = stock.get("marketCap", 0.0)
        fiftyDayAverage = stock.get("fiftyDayAverage", 0.0)
        
        stockObject= stockUnit(stockId, ticker, currentPrice, openPrice, closePrice, change, mCap, fiftyDayAverage)
        stockList.append(stockObject)

        
    return stockList
