class stockUnit:
    def __init__(self, 
                stockId,
                ticker, 
                currentPrice, 
                openPrice, 
                closePrice, 
                change, 
                mCap, 
                fiftyDayAverage):
        self.stockId = stockId
        self.ticker = ticker
        self.currentPrice = currentPrice
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.change = change
        self.mCap = mCap
        self.fiftyDayAverage = fiftyDayAverage
    
    def __str__(self):
        return (
            f"Id: {self.stockId}, "
            f"Ticker: {self.ticker}, "
            f"Current Price: {self.currentPrice}, "
            f"Market Open Price: {self.openPrice}, "
            f"Market Close Price: {self.closePrice}, "
            f"Change Percent: {self.change}%, "
            f"Market Cap: {self.mCap}, "
            f"Fifty Day Average: {self.fiftyDayAverage}, "
        )

class cryptoUnit:
    def __init__(self,
                coinId, 
                symbol, 
                currentPrice, 
                low24, 
                high24, 
                fluct, 
                circSupp, 
                mCap, 
                updateDate,
                marketCapRank):
        self.symbol= symbol
        self.coinId= coinId
        self.currentPrice= currentPrice
        self.low24= low24
        self.high24= high24
        self.fluct= fluct
        self.circSupp= circSupp
        self.mCap= mCap
        self.updateDate= updateDate
        self.marketCapRank= marketCapRank
        
    def __str__(self):
        return (
            f"Symbol: {self.symbol}, "
            f"ID: {self.coinId}, "
            f"Current Price: {self.currentPrice}, "
            f"Lowest Price (Last 24 hours): {self.low24}, "
            f"Highest Price (Last 24 hours): {self.high24}, "
            f"Fluctuations in Price (Last 24hrs): {self.fluct}, "
            f"Circulating Supply: {self.circSupp}, "
            f"Market Cap: {self.mCap}, "
            f"Last Update Date: {self.updateDate}, "
            f"Market Cap Rank: {self.marketCapRank}, "
        )
        