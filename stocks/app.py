from flask import Flask, render_template
from getCryptoData import  startCollectCrypto
from getStockData import startCollectStock
from dataVisualise import getData

app = Flask(__name__)

@app.route('/')
def dataPresent():
    # Collect stock and crypto data
    stockInfo = startCollectStock()  # This should return a list of stockUnit objects
    cryptoInfo = startCollectCrypto()  # This should return a list of cryptoUnit objects
    graphInfo = getData()


    # Render the template with the data
    return render_template("index.html", stockInfo=stockInfo, cryptoInfo=cryptoInfo, graphInfo=graphInfo)


if __name__ == "__main__":
   app.run(debug=True)
