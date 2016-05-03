#!/usr/local/bin/python

import os, sys, csv
import random
from datetime import date, timedelta

i=1;
file = ""
while 1==1:

  tradeid = i
  description = ''.join(random.sample('ABCDEFGHIJKLM1234567890@#',15))
  tradedate = date.today()
  settlementdate = tradedate + timedelta(days=5)
  traderid = random.randint(1,100)
  brokerid = random.randint(1,20)
  cusip = ''.join(random.sample('ABCDEFGHIJKLM1234567890@#',9))
  settlementamount = random.randint(1,999999999)
  count = random.randint(1,1000000)

  print tradeid.__str__() + "|" + description + "|" + tradedate.__str__() + "|" + settlementdate.__str__()  + "|" + tradeid.__str__()  + "|" + brokerid.__str__()   + "|" + cusip.__str__()  + "|" +  settlementamount.__str__()  + "|" +  count.__str__()
  line = tradeid.__str__() + "|" + description + "|" + tradedate.__str__() + "|" + settlementdate.__str__()  + "|" + tradeid.__str__()  + "|" + brokerid.__str__()   + "|" + cusip.__str__()  + "|" +  settlementamount.__str__()  + "|" +  count.__str__()
  """file = file + '\n' + line"""
  i=i+1

else:
  print "done"

