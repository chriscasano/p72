CREATE DATABASE P72;

USE P72;

CREATE EXTERNAL TABLE TRADES_ORC
{
TRADEID                         STRING,
DESCRIPTION             STRING,
TRADEDATE                       DATE,
SETTLEMENTDATE          DATE,
TRADERID                        STRING,
BROKERID                        STRING,
CUSIP                           STRING,
SETTLEMENTAMOUNT        FLOAT,
COUNT                           INT
}
STORED AS ORC
TBLPROPERTIES ("orc.compress"="SNAPPY")
;

CREATE EXTERNAL TABLE P72.TRADES2_ORC
(
TRADEID                         STRING,
DESCRIPTION             STRING,
SETTLEMENTDATE          DATE,
TRADERID                        STRING,
BROKERID                        STRING,
CUSIP                           STRING,
SETTLEMENTAMOUNT        FLOAT,
COUNT                           INT
)
PARTITIONED BY (TRADEDATE DATE)
STORED AS ORC
LOCATION '/user/ec2-user/data/trades2_orc'
TBLPROPERTIES ("orc.compress"="SNAPPY")
;


SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.exec.dynamic.partition=true;


INSERT INTO TABLE P72.TRADES2_ORC PARTITION(TRADEDATE)
SELECT TRADEID, DESCRIPTION, SETTLEMENTDATE, TRADERID, BROKERID, CUSIP, SETTLEMENTAMOUNT, COUNT, TRADEDATE
FROM P72.TRADES_STG WHERE TRADEID < 9000000001;
