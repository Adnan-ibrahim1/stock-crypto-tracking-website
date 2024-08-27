import requests
from storeUnit import cryptoUnit

def startCollectCrypto():
    url= 'https://api.coingecko.com/api/v3/coins/markets'
    params= {
        'vs_currency': 'eur',
        "order": 'volume_desc',
        'per_page': 25,
        'page': 1
    }
    
    response= requests.get(url, params= params)
    data= response.json()
    return collectCryptoData(data)

def collectCryptoData(data):
    currencyList= []
    
    for coin in data:
        coinId= coin["id"]
        symbol= coin["symbol"]
        currentPrice= coin["current_price"]
        low24= coin["low_24h"]
        high24= coin["high_24h"]
        fluct= coin["price_change_percentage_24h"]
        circSupp= coin["circulating_supply"]
        mCap= coin["market_cap"]
        updateDate= coin["last_updated"]
        marketCapRank= coin["market_cap_rank"]
        
        cryptoObject= cryptoUnit(coinId, symbol, currentPrice, low24, high24, fluct, circSupp, mCap, updateDate, marketCapRank)
        currencyList.append(cryptoObject)
        
    return currencyList