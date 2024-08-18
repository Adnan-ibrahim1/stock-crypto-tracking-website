from flask import *
import getCryptoData as gcd
import getStockData as gsd

trackerApp= Flask(__name__)

@trackerApp.route("/")
def dataPresent():
    return render_template("")
# should be the front page
# has two boxes (stocks / crypto) in the middle
# 

# @trackerApp.route("/stocks")
# def stocksPresent():
#     stockInfo= gsd.startCollectStock()
#     return render_template("", stockInfo= stockInfo)
#     pass

# @trackerApp.route("/crypto")
# def cryptoPresent():
#     cryptoInfo= gcd.startCollectCrypto()
#     return render_template("", cryptoInfo= cryptoInfo)
#     pass
    
if __name__ == "__main__":
    trackerApp.run(debug= False)