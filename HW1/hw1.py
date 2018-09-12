import re
import sys
from pyspark import SparkConf, SparkContext

def make_pseudo_friends(t):
	friends = t[1]
	pairs = []
	for i in range(0, len(friends)):
		for j in range(i+1, len(friends)):
			if friends[i] < friends[j]:
				pairs.append([friends[i], friends[j], False])
			else:
				pairs.append([friends[j], friends[i], False])
	return pairs

conf = SparkConf()
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1])

tuples = lines.map(lambda l: l.split('\t'))
tuples = tuples.map(lambda l: (l[0], l[1].split(',')))

pseudo_friends = tuples.flatMap(make_pseudo_friends)

print(pseudo_friends.collect())
for _ in range(3):
	print('\n')
