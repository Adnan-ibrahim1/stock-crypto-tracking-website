from flask import Flask, render_template
import getCryptoData as gcd
import getStockData as gsd

trackerApp = Flask(__name__)

@trackerApp.route("/")
def dataPresent():
    stockInfo = gsd.startCollectStock()
    cryptoInfo = gcd.startCollectCrypto()
    return render_template("index.html", stockInfo=stockInfo, cryptoInfo=cryptoInfo)

if __name__ == "__main__":
    trackerApp.run(debug=False)
