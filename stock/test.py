def trend(day, price, n):
	change = []
	previous = ''
	previous_price = ''
	for i in xrange(n-1):
		print i, previous_price
		if price[i+1] != 'missing':
			if previous_price == '':
				diff = price[i+1] - price[i]
			else:
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
	print change
	return change

day = []
price = [1,2,'missing',1,'missing',0,5,7]
n = len(price)
trend(day,price,n)