from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import RandomForestClassifier
import numpy as np
import json

def benchmark(clf,X,y,X_test,name):
	clf.fit(X,y)
	pred_test = clf.predict(X_test)
	
	pred_actual = clf.predict(X)
	wrong = sum([pred_actual[i] != y[i] for i in xrange(len(y))])
	return pred_test, wrong

def classifier(x, group, x_test):
	vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english',ngram_range=(1, 2))
	X = vectorizer.fit_transform(x)
	y = np.array(group)
	X_test = vectorizer.transform(x_test)
	
	'''
	results = []
	for clf, name in (
        (RidgeClassifier(tol=1e-2, solver="sag"), "Ridge Classifier"),
        (Perceptron(n_iter=50), "Perceptron"),
        (PassiveAggressiveClassifier(n_iter=50), "Passive-Aggressive"),
		(MultinomialNB(alpha=0.01), "multinomialNB")):
		results.append(benchmark(clf,X,y,X_test,name))
	print results
	'''
	clf = PassiveAggressiveClassifier(n_iter=50)
	name = "Perceptron"
	prediction, wrong = benchmark(clf,X,y,X_test,name)
	for answer in prediction:
		print answer
	

if __name__ == '__main__':
	x,y = [],[]
	with open('training.json','r') as f:
		t = int(f.readline())
		for _ in xrange(t):
			temp = json.loads(f.readline())
			x.append(temp['question'] + ' ' + temp['excerpt'])
			y.append(temp['topic'])
			
	x_test = []
	n = int(raw_input())
	for _ in xrange(n):
		temp = json.loads(raw_input())
		x_test.append(temp['question'] + ' ' + temp['excerpt'])
		
	classifier(x,y,x_test)