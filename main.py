import yfinance as yf

aktien = ['AMZN', 'MSFT', 'GOOGL', 'META', 'TSLA', 'NVDA', 'JNJ', 'JPM', 'V', 'PG', 'HD', 'MA', 'UNH', 'PYPL', 'ADBE', 'NFLX', 'CRM', 'ABT', 'TXN', 'PFE', 'BMY', 'COST', 'AVGO', 'MCD', 'AMGN', 'CSCO', 'MDT', 'UNP', 'LLY', 'ORCL', 'NKE', 'VZ', 'SBUX', 'DHR', 'ABBV', 'QCOM', 'IBM', 'MMM', 'NOW', 'MO', 'AMD', 'TMUS', 'TMO', 'INTU', 'SPGI', 'CI', 'AEP', 'GM', 'AIG', 'LMT', 'BKNG', 'TM', 'CVS', 'ADP', 'NEE', 'PLD']

for ticker in aktien:
    aktie = yf.Ticker(ticker)
    letzter_schlusskurs = aktie.history(period='1d')['Close'].iloc[-1]
    print(f"Aktie: {ticker}, Letzter Schlusskurs: {letzter_schlusskurs}")
