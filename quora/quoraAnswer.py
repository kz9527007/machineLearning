import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def vectorizer(x,y):
	#logistic = LogisticRegression()
	#logistic.fit(x,y)
	
	clf = RandomForestClassifier(n_estimators=10)
	clf.fit(x,y)
	return clf

if __name__ == '__main__':
	n,m = map(int, raw_input().split())
	x = []
	y = []
	for i in xrange(n):
		temp = raw_input().split()
		y_temp = int(temp[1])
		if y_temp == 1:
			y.append(1)
		else:
			y.append(0)
		x.append([])
		for item in temp[2::]:
			x[i].append(float(item.split(':')[1]))
	exclude = []
	for i in xrange(m):
		xx = [x[j][i] for j in xrange(n)]
		if np.mean(xx) == min(xx) and np.mean(xx) == max(xx):
			exclude.append(i)
	# Based on this analysis, we do not need to use 
	
	x_train = []
	for i in xrange(n):
		x_train.append([x[i][j] for j in xrange(m) if j not in exclude])
	#print x_train[0:5]
	#print y[0:15]
	clf = vectorizer(x_train,y)
	
	# Read test files
	t = int(raw_input())
	x_test = []
	id = []
	for i in xrange(t):
		temp = raw_input().split()
		id.append(temp[0])
		x_test.append([])
		for index, item in enumerate(temp[1::]):
			if index not in exclude:
				x_test[i].append(float(item.split(':')[1]))
	
	y_test = clf.predict(x_test)
	
	for j in xrange(t):
		temp = y_test[j]
		if temp == 0:
			output = '-1'
		else:
			output = '+1'
		print id[j] + ' ' + output