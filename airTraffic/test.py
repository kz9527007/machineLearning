import numpy as np
#import pylab as pl
#import random
    
def average(x):
	return sum(x)/len(x)
	
def main():
	#fid = open('input.txt')
	n = int(raw_input())
	x = []
	for _ in xrange(n):
		x.append(float(raw_input().split()[1]))
	x = np.array(x)

	n_predict = 12
	
	for i in xrange(len(x)/12):
		temp = x[12*i:12*(i+1)]
		#print average(temp)
		#pl.plot(np.arange(12), temp, label = str(i))
	month = []
	for i in xrange(12):
		temp = [x[12*j+i] for j in xrange(n/n_predict)]
		month.append(average(temp))
	monthall = average(month)
	month = [(xx/monthall)**2*1.2 for xx in month]
	#print month
	s0p, s60p, s80p, s100p, s120p, s140p, s160p = [], [], [], [], [], [], []
	s0n, s60n, s80n, s100n, s120n, s140n, s160n = [], [], [], [], [], [], []
	upup, updown, downdown, downup = 0.0, 0.0, 0.0, 0.0
	previous = x[0]
	previous_d = 0
	for i in x[1::]:
		diff = i-previous
		#print previous, i, diff
		if previous < 600000:
			if diff > 0:
				s0p.append(diff)
			else:
				s0n.append(diff)
		elif previous < 800000:
			if diff > 0:
				s60p.append(diff)
			else:
				s60n.append(diff)
		elif previous < 1000000:
			if diff > 0:
				s80p.append(diff)
			else:
				s80n.append(diff)
		elif previous < 1200000:
			if diff > 0:
				s100p.append(diff)
			else:
				s100n.append(diff)
		elif previous < 1400000:
			if diff > 0:
				s120p.append(diff)
			else:
				s120n.append(diff)
		elif previous < 1600000:
			if diff > 0:
				s140p.append(diff)
			else:
				s140n.append(diff)
		else:
			if diff > 0:
				s160p.append(diff)
			else:
				s160n.append(diff)
		if previous_d != 0:
			if previous_d > 0 and diff > 0:
				upup += 1
			elif previous_d > 0 and diff < 0:
				updown += 1
			elif previous_d < 0 and diff < 0:
				downdown += 1
			else:
				downup += 1
		else:
			previous_d = diff
		previous = i
	
	for j in xrange(12):
		#print diff
		option = 0
		monthEffect = month[(n+j) % 12]
		if previous < monthall:
			option = 1
		
		if option == 1:
			if previous < 600000:
				ans = (previous + average(s0p)) * monthEffect
			elif previous < 800000:
				ans = (previous + average(s60p)) * monthEffect
			elif previous < 1000000:
				ans = (previous + average(s80p)) * monthEffect
			elif previous < 1200000:
				ans = (previous + average(s100p)) * monthEffect
			elif previous < 1400000:
				ans = (previous + average(s120p)) * monthEffect
			elif previous < 1600000:
				ans = (previous + average(s140p)) * monthEffect
			else:
				ans = (previous + average(s160p)) * monthEffect
		else:
			if previous < 600000:
				ans = (previous + average(s0n)) * monthEffect
			elif previous < 800000:
				ans = (previous + average(s60n)) * monthEffect
			elif previous < 1000000:
				ans = (previous + average(s80n)) * monthEffect
			elif previous < 1200000:
				ans = (previous + average(s100n)) * monthEffect
			elif previous < 1400000:
				ans = (previous + average(s120n)) * monthEffect
			elif previous < 1600000:
				ans = (previous + average(s140n)) * monthEffect
			else:
				ans = (previous + average(s160n)) * monthEffect
		diff = ans - previous
		print ans
	#pl.legend()
	#pl.show()
	
if __name__ == "__main__":
    main()