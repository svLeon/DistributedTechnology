import sys, glob
import urlparse
import urllib
import re

sys.path.append('gen-py')

from root import Root
from root.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class RootHandler:
   def root(self , s):
      hostname = urlparse.urlparse(s).hostname.split(".")
      hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
      return hostname

   def links(self, s):
      website = urllib.urlopen(s)
      html = website.read()
      links = re.findall('"((http|ftp)s?://.*?)"', html)
      l = []
      for link in links :
         l.append(self.root(link[0]))
      l = list(set(l))
      return l

handler = RootHandler()
processor = Root.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor , transport , tfactory, pfactory)
server.serve()
