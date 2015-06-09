# coding: utf8
import sys
import os 
from operator import add
from pyspark import SparkContext
from collections import Counter
import math

sc = SparkContext(appName="WordStat")

files = sc.wholeTextFiles(sys.argv[1])
doc = ''.join(sys.argv[2])
folder = ''.join(sys.argv[1]) + '/'
N = float(files.count())

statistics = files.map(lambda x: (x[0].split(folder)[1].encode('utf-8') , x[1].split())) \
	      .flatMap(lambda x: ((w.encode('utf-8') , Counter({x[0]: 1})) for w in x[1])) \
	      .reduceByKey(lambda a, b: a + b) \
	      .flatMap(lambda x: ((doc, [(x[0], (count * math.log(N / len(x[1]))))]) for doc, count in x[1].items()))\
	      .reduceByKey(lambda a, b: a + b)
              
output = statistics.collect()

for pair in output:
	if pair[0] == doc :
		print '----------------------------------------------'
		print 'Document ' + doc
		words = sorted(pair[1], key = lambda y : y[1], reverse = True)
		k = min(len(pair[1]), 10)
		words = words[:k:]
		for word in words:
			print '( ' + word[0] + ' , ', word[1], ' )'
		print '----------------------------------------------'


sc.stop()
