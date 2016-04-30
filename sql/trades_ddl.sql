CREATE DATABASE P72;

USE P72;

CREATE EXTERNAL TABLE TRADES
{
TRADEID 			STRING,
DESCRIPTION 		STRING,
TRADEDATE 			DATE,
SETTLEMENTDATE 		DATE,
TRADERID 			STRING,
BROKERID 			STRING,
CUSIP 				STRING,
SETTLEMENTAMOUNT 	FLOAT,
COUNT 				INT
}
STORED AS ORC
TBLPROPERTIES ("orc.compress"="SNAPPY")
;