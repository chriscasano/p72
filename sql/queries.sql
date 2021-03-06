
// AGGREGATIONS

SELECT TRADEDATE, CUSIP, BROKERID, COUNT(*), SUM(SETTLEMENTAMOUNT)
FROM P72.TRADES
GROUP BY TRADEDATE, CUSIP, BROKERID
;

SELECT WEEKOFYEAR(TRADEDATE), CUSIP, BROKERID, COUNT(*), SUM(SETTLEMENTAMOUNT)
FROM P72.TRADES	
GROUP BY WEEKOFYEAR(TRADEDATE), CUSIP, BROKERID
;

SELECT COUNT(DISTINCT TRADERID)
FROM P72.TRADES
GROUP BY TRADEDATE
;

SELECT COUNT(DISTINCT TRADERID)
FROM P72.TRADES
GROUP BY WEEKOFYEAR(TRADEDATE)
;

// INTERACTIVE QUERY

SELECT AVG(DIFF), MEDIAN(DIFF), STDDEV(DIFF)
FROM
(
	SELECT BROKERID, DATEDIFF(TRADEDATE, SETTLEMENTDATE) AS DIFF
	FROM P72.TRADES
);

SELECT COUNT(*)
FROM P72.TRADES
WHERE REGEX(DESCRIPTION, "(HDP|HDF)")
