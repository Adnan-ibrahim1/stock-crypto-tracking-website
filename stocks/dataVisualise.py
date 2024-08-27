import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive plotting
import matplotlib.pyplot as plt
import yfinance as yf
import os
from getStockData import startCollectStock

# Directory to save images
IMAGE_DIR = 'static/images'

def getData():
    stockList = startCollectStock()
    tickers = [stock.ticker for stock in stockList]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    plot_files = []
    for ticker in tickers:
        all_data = yf.Ticker(ticker)
        hist = all_data.history(period="1mo", interval="1d")
        histClose = hist["Close"]
        dates = hist.index

        filename = createPlot(ticker, dates, histClose)
        plot_files.append(filename)
    
    return plot_files

def createPlot(stock, dates, closePrice):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, closePrice, marker="o", linestyle="-", color="green")
    plt.title(f"{stock}")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = f"{stock}.png"
    filepath = os.path.join(IMAGE_DIR, filename)
    plt.savefig(filepath)
    plt.close()

    return filename
