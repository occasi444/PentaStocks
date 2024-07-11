import sqlite3
import yfinance as yf

verbindung = sqlite3.connect("datenbanken/ticker.db")
zeiger = verbindung.cursor()

zeiger.execute("SELECT * FROM ticker")
daten = zeiger.fetchall()

for ticker in daten:
    ticker_symbol = ticker[0]
    data = yf.Ticker(ticker_symbol)
    current_price = data.history(period="1d")["Close"].iloc[-1]
    print(f"Aktueller Preis für {ticker_symbol}: {current_price}")

verbindung.close()