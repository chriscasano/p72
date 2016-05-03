

#!/usr/bin/env python26

"""Python HDFS use examples.
After reading this example you should have enough information to read and write
HDFS files from your programs.
"""


import time
from datetime import date, timedelta
import random
from hdfs.hfile import Hfile

hostname = 'sandbox.hortonworks.com'
port = 8020
hdfs_path = '/tmp'
hfile = Hfile(hostname, port, hdfs_path, mode='w')

i=1;
while i < 100:

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

  hfile.write(line)

  i=i+1

else:
  print "done"


hfile.close()

"""
# Let's read local_path into memory for comparison.
motd = open(local_path).read()

# Now let's read the data back
hfile = Hfile(hostname, port, hdfs_path)

# With an iterator
data_read_from_hdfs = ''
for line in hfile:
  data_read_from_hdfs += line
print motd == data_read_from_hdfs

# All at once
data_read_from_hdfs = hfile.read()
print motd == data_read_from_hdfs

hfile.close()

# Hopefully you have enough info to get started!

from hdfs.hfilesystem import Hfilesystem
hfs = Hfilesystem(hostname, port)
print hfs.getHosts(hdfs_path, 0, 1)
"""