create table `stocks` (
    `symbol` varchar(10) NOT NULL COMMENT "stock symbol",
    `date` date NOT NULL COMMENT "date",
    `price` float NOT NULL COMMENT "stock price"
)
COMMENT "stock data"