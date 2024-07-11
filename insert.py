import sqlite3
verbindung = sqlite3.connect("datenbanken/ticker.db")
zeiger = verbindung.cursor()

sql_anweisung = """
CREATE TABLE IF NOT EXISTS ticker (
ticker VARCHAR(20)
);"""

zeiger.execute(sql_anweisung)

sql_anweisung = """
INSERT INTO ticker VALUES ('AMZN'), ('MSFT'), ('GOOGL'), ('META'), ('TSLA'), ('NVDA'), ('JNJ'), ('JPM'), ('V'), ('PG'), ('HD'), ('MA'), ('UNH'), ('PYPL'), ('ADBE'), ('NFLX'), ('CRM'), ('ABT'), ('TXN'), ('PFE'), ('BMY'), ('COST'), ('AVGO'), ('MCD'), ('AMGN'), ('CSCO'), ('MDT'), ('UNP'), ('LLY'), ('ORCL'), ('NKE'), ('VZ'), ('SBUX'), ('DHR'), ('ABBV'), ('QCOM'), ('IBM'), ('MMM'), ('NOW'), ('MO'), ('AMD'), ('TMUS'), ('TMO'), ('INTU'), ('SPGI'), ('CI'), ('AEP'), ('GM'), ('AIG'), ('LMT'), ('BKNG'), ('TM'), ('CVS'), ('ADP'), ('NEE'), ('PLD');
"""

zeiger.execute(sql_anweisung)

verbindung.commit()
verbindung.close()

