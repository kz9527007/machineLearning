from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import RandomForestClassifier
import numpy as np


def benchmark(clf,X,y,X_test,name):
	clf.fit(X,y)
	pred_test = clf.predict(X_test)
	
	pred_actual = clf.predict(X)
	wrong = sum([pred_actual[i] != y[i] for i in xrange(len(y))])
	return pred_test, wrong

def classifier(x, group, x_test):
	vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')
	X = vectorizer.fit_transform(x)
	y = np.array(group)
	X_test = vectorizer.transform(x_test)
	print x_test
	print X_test
	print y
	'''
	results = []
	for clf, name in (
        (RidgeClassifier(tol=1e-2, solver="sag"), "Ridge Classifier"),
        (Perceptron(n_iter=50), "Perceptron"),
        (PassiveAggressiveClassifier(n_iter=50), "Passive-Aggressive"),
        (KNeighborsClassifier(n_neighbors=10), "kNN"),
		(MultinomialNB(alpha=0.01), "multinomialNB")):
		results.append(benchmark(clf,X,y,X_test,name))
	results = [14,7,7,351,46]
	'''
	clf = PassiveAggressiveClassifier(n_iter=50)
	name = "Passive-Aggressive"
	prediction, wrong = benchmark(clf,X,y,X_test,name)
	for answer in prediction:
		print answer

def main():
	group, x = [], []

	with open('trainingdata.txt', 'r') as f:
		t = int(f.readline())
		for _ in xrange(t):
			temp = f.readline()
			group.append(temp[0])
			x.append(temp[2::])
	'''
	x_test = []
	n = int(raw_input())
	for _ in xrange(n):
		x_test.append(raw_input())
	'''
	x_test = ['This is a document','this is another document','documents are seperated by newlines']
	classifier(x, group, x_test)
			
if __name__ == '__main__':
	main()