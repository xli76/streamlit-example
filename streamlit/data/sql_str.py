create_sql = """
CREATE TABLE IF NOT EXISTS stocks (
    symbol varchar(10) NOT NULL COMMENT "stock symbol",
    date date NOT NULL COMMENT "date",
    price float NOT NULL COMMENT "stock price"
)
COMMENT "stock data"
"""
insert_sql = "INSERT INTO stocks (symbol, date, price) VALUES (%s, %s, %s)"
stock_sql = "select symbol, date, price from stocks"