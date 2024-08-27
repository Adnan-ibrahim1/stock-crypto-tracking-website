from flask import Flask, render_template
from getCryptoData import startCollectCrypto
from getStockData import startCollectStock
from dataVisualise import getData
import os

app = Flask(__name__)

# Directory to save images
IMAGE_DIR = 'static/images'

@app.route('/')
def dataPresent():
    # Collect stock and crypto data
    stockInfo = startCollectStock()  # This should return a list of stockUnit objects
    cryptoInfo = startCollectCrypto()  # This should return a list of cryptoUnit objects
    
    # Ensure the directory for images exists
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    # Generate and save plots
    graphInfo = getData()  # getData should save images and return a list of filenames

    # Render the template with the data
    return render_template("index.html", stockInfo=stockInfo, cryptoInfo=cryptoInfo, graphInfo=graphInfo)

if __name__ == "__main__":
    app.run(debug=True)
