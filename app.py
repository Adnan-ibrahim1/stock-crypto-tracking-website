from flask import Flask, render_template
from getCryptoData import  startCollectCrypto
from getStockData import startCollectStock

app = Flask(__name__)

@app.route('/')
def dataPresent():
    
    stockInfo = startCollectStock()
    cryptoInfo = startCollectCrypto()

    return render_template("index.html", stockInfo=stockInfo, cryptoInfo=cryptoInfo)


if __name__ == "__main__":
   app.run(debug=True)
