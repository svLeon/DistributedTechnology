import sys, glob
from collections import Counter

sys.path.append('gen-py')

from root import Root
from root.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try :
   transport = TSocket.TSocket('localhost', 9090)
   transport = TTransport.TBufferedTransport(transport)
   protocol = TBinaryProtocol.TBinaryProtocol(transport)
   client = Root.Client(protocol)
   transport.open()
   
   allRoots = []
   file = open("sites.txt", "r")
   l = file.readline()
   print 'Open file sites.txt :'
   while(len(l) > 1):
      print '-----------'
      print 'Site :'
      print l
      links = client.links(l)
      allRoots.extend(links)
      for link in links :
         print link 
      l = file.readline()
   
   print 'all sites : '
   for x in set(allRoots) :
      print x + ' : ' + str(allRoots.count(x))

   transport.close()
except Thrift.TException , tx:
   print '%s' % (tx.message)
