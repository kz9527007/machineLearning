from datetime import date
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

if __name__ == '__main__':
	n = int(raw_input())
	#with open('input.txt') as f:
	#	n = int(f.readline())
	train, test, y = [], [], []
	for i in xrange(n):
		temp = raw_input().split()
		current = map(int, temp[0].split('/'))			
		if 'Missing' not in temp[-1]:
			train.append((current[0], current[1]))
			y.append(float(temp[-1]))
		else:
			test.append((current[0], current[1]))
	model = GradientBoostingRegressor()
	model.fit(train,y)
	
	predict_stock = model.predict(test)
	print '\n'.join([str(x) for x in predict_stock])