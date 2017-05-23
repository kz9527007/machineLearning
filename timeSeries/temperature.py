import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
	
if __name__ == '__main__':
	n = int(raw_input())
	
	#with open('temperature.txt') as f:
	#	n = int(f.readline())
	#columns = f.readline().split()
	columsn = raw_input().split()
	train_max, train_min, test_max, test_min, y_max, y_min = [], [], [], [], [], []
	miss = []
	month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
	for _ in xrange(n):
		#temp = f.readline().split()
		temp = raw_input().split()
		y,m = int(temp[0]),month[temp[1]]
		#m.append(month[temp[1]])
		if 'Missing' in temp[2]:
			nn = len(test_max)
			test_max.append((y,m,float(temp[3])))
			miss.append((0,nn))
		elif 'Missing' in temp[3]:
			nn = len(test_min)
			test_min.append((y,m,float(temp[2])))
			miss.append((1,nn))
		else:
			train_max.append((y,m,float(temp[3])))
			train_min.append((y,m,float(temp[2])))
			y_max.append(float(temp[2]))
			y_min.append(float(temp[3]))

	model_max = GradientBoostingRegressor(loss='huber',n_estimators=500)
	model_max.fit(train_max,y_max)
	
	model_min = GradientBoostingRegressor(loss='huber',n_estimators=500)
	model_min.fit(train_min,y_min)
	
	predict_max = model_max.predict(test_max)
	predict_min = model_min.predict(test_min)
	
	for index, i in miss:
		if index == 0:
			print predict_max[i]
		else:
			print predict_min[i]
	