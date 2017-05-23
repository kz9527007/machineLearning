import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

def vector(X_train, y_train):
	vectorizer = TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)
	
	#clf = PassiveAggressiveClassifier(n_iter=100)
	#clf = MultinomialNB(alpha=0.05)
	clf = LinearSVC(C=1.5)
	
	pipeline = Pipeline([('prep', vectorizer), ('clf', clf)])
	
	pipeline.fit(X_train, y_train)
	#clf.fit(X_train, y_train)
	#print pipeline.score(X_test,y_test)
	return pipeline
	

if __name__ == "__main__":
	with open('training.json') as f:
		n = int(f.readline())
		
		x, y = [], []
		for _ in xrange(n):
			temp = json.loads(unicode(f.readline().lower(),'utf8'))
			x.append((temp['section'] + ' ')*10 + temp['heading'])
			y.append(temp['category'])
	#print y[0:10]
	clf = vector(x,y)
	
	n = int(raw_input())
	x_test = []
	for _ in xrange(n):
		#a = '{"city":"chicago","section":"for-sale","heading":"Madden NFL 25 XBOX 360. Brand New!"}'
		temp = json.loads(unicode(raw_input().lower(),'utf8'))
		x_test.append((temp['section'] + ' ')*10 + temp['heading'])
	print '\n'.join(clf.predict(x_test))
	