from datetime import date
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

def trend(day, price, n):
	change = []
	previous = ''
	previous_price = 0
	for i in xrange(n-1):
		if price[i+1] != 'missing':
			diff = price[i+1] - previous_price
			if i == 0:
				previous = (diff > 0)
			else:
				current = (diff > 0)
				if diff != 0:
					if previous != current:
						change.append(i+1)
				previous = current
			previous_price = price[i+1]
		else:
			if previous == '':
				previous = True
	return change

def fillMissing(day,price,n,change):
	missing = [x for x in xrange(n) if price[x] == 'missing']
	print 'missing', missing
	output = []
	for m in missing:
		if m == 0 or m < change[0]:
			start = 1
			last = change[0]
		elif m == n:
			start = change[-1]
			last = n-1
		else:
			print day[m], max(change)
			if m > max(change):
				last = m - 1
				start = max(change)
				if start == last:
					start -= 1
			else:
				last = [x for x in change if x > m][0]
				start = change[change.index(last)-1]
				print start, last, 'initial'
				if last - start < 2:
					start = change[change.index(last)-1]
		print m, day[m], start, last
		
		X, y = [], []
		for i in xrange(day[start], day[last]):
			if i in day:
				if price[day.index(i)] != 'missing':
					X.append(i)
					y.append(price[day.index(i)])
		if len(X) > 1:
			print X
			print y
			slope = (y[-1] - y[0]) / (X[-1] - X[0])
			output.append(slope*(day[m] - X[0]) + y[0])
		else:
			while True:
				if price[m] != 'missing':
					output.append(price[m])
					break
				else:
					m -= 1
	print '\n'.join([str(x) for x in output])		
			
	
if __name__ == '__main__':
	
	with open('input.txt') as f:
		n = int(f.readline())
		day, price = [], []
		for i in xrange(n):
			temp = f.readline().split()
			current = map(int, temp[0].split('/'))
			if i == 0:
				day.append(0)
				previous = date(current[2],current[0],current[1])
			else:
				d0 = previous
				d1 = date(current[2],current[0],current[1])
				delta = d1 - d0
				day.append(delta.days)
			
			if 'Missing' not in temp[-1]:
				price.append(float(temp[-1]))
			else:
				price.append('missing')
	'''
	n = int(raw_input())
	day, price = [], []
	for i in xrange(n):
		temp = raw_input().split()
		current = map(int, temp[0].split('/'))
		if i == 0:
			day.append(0)
			previous = date(current[2],current[0],current[1])
		else:
			d0 = previous
			d1 = date(current[2],current[0],current[1])
			delta = d1 - d0
			day.append(delta.days)
		
		if 'Missing' not in temp[-1]:
			price.append(float(temp[-1]))
		else:
			price.append('missing')
	'''		
	change = trend(day, price, n)
	print change
	fillMissing(day,price,n,change)