# aggregate articles

import pickle
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

f = open('article_data.dat')
data = pickle.load(f)
f.close()

print "calculating most common words..."
words = Counter()
for article in data:
	tokens = nltk.word_tokenize(article['description'])
	tokens = filter(lambda x: not x in stopwords.words('english'), tokens)
	tokens = nltk.pos_tag(tokens)
	tokens = [t[0] for t in tokens if ( t[1] == "NN" or t[1] == "NNP")]
	words.update(tokens)

print "%r" % words.most_common(200)