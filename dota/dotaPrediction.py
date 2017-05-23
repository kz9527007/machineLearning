from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn.metrics import accuracy_score

def vectorizer(x,y):
	clf = RandomForestClassifier(n_estimators=10)
	clf.fit(x,y)
	return clf

def main():
	fid = open('trainingdata.txt')
	heros = []
	x_train = []
	y_train = []
	for line in fid:
		x = [0] * 100
		temp = line.split(',')
		result = int(temp[-1])
			
		for hero in temp[0:5]:
			if hero not in heros:
				heros.append(hero)
			x[heros.index(hero)] = 1
		for hero in temp[5:10]:
			if hero not in heros:
				heros.append(hero)
			x[heros.index(hero)] = -1
		
		x_train.append(x)
		y_train.append(result-1)
	
	for ii in xrange(10):
		xx_train, xx_test, yy_train, yy_test = train_test_split(x_train, y_train, test_size=0.10, random_state=42)
		clf = vectorizer(xx_train,yy_train)
		print ii, accuracy_score(clf.predict(xx_test), yy_test)
			
	'''		
	t = int(raw_input())
	
	x_test = []
	for _ in xrange(t):
		x = [0] * 100
		temp = raw_input().split(',')
		for hero in temp[0:5]:
			if hero not in heros:
				heros.append(hero)
			x[heros.index(hero)] = 1
		for hero in temp[5:10]:
			if hero not in heros:
				heros.append(hero)
			x[heros.index(hero)] = -1
		
		x_test.append(x)

	y_test = clf.predict(x_test)
	for result in y_test:
		print result + 1
	'''	
if __name__ == '__main__':
	main()