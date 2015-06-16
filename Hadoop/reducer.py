# coding: utf8
import sys
from collections import defaultdict
 
last_key = None
running_total = 0

bigram = defaultdict(int)
trigram = defaultdict(int)

for input_line in sys.stdin:
   input_line = input_line.strip()
   first, value = input_line.split("\t", 1)
   first = first.strip()
   vals = value.split("', '")
   second = vals[0].lstrip("['")
   third = vals[1].rstrip("']")
   bigram[(first, second)] += 1
   bigram[(second, third)] += 1
   trigram[(first, second, third)] += 1

for t, f3 in trigram.items():
      f2 = bigram.get(t[1:], 0)
      if f2 == 0:
        p = 0
      else:
        p = float(f3) / float(f2)
      print t, '\t', (f3, f2, p)

