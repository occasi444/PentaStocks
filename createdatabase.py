import yfinance as yf
import matplotlib.pyplot as plt

class StockAnalysis:
 def __init__(self, ticker_symbols):
     self.tickers = [yf.Ticker(symbol) for symbol in ticker_symbols]

 def plot_stock_prices(self, period):
     plt.figure(figsize=(12, 8))
     for ticker in self.tickers:
         hist = ticker.history(period=period)
         plt.plot(hist['Close'], label=ticker.info['longName'])

     plt.title('Aktienkursentwicklung letztes Jahr')
     plt.xlabel('Datum')
     plt.ylabel('Schlusskurs')
     plt.legend()
     plt.show()

# Beispielaufruf
stock_symbols = ["NVDA", "AAPL", "GOOGL"]  # Beispiel für mehrere Ticker-Symbole
stock_analysis = StockAnalysis(stock_symbols)
stock_analysis.plot_stock_prices("1y")