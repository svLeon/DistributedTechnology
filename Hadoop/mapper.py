# coding: utf8
import sys

keys = [] 
for line in sys.stdin:
   line = line.strip()
   keys = keys + line.split()
   n = len(keys)
   
for i in range(0, n):
      if i > n - 3:
        break

      first = keys[i].lower().strip(' \t\n\r.,;:')
      second_third = []
      for j in range(i+1, i+3):
        second_third.append(keys[j].lower().strip(' \t\n\r.,;:'))

      print first, '\t', second_third

