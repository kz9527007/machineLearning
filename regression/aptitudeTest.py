def pearson(x,y,n):
	dem = n*sum([x[i]*y[i] for i in xrange(n)]) - sum(x)*sum(y)
	num_1 = n*sum([i**2 for i in x]) - sum(x)**2
	num_2 = n*sum([j**2 for j in y]) - sum(y)**2
	if num_1 * num_2 != 0:
		return dem / (num_1**0.5 * num_2**0.5)
	else:
		return 0
	
if __name__ == '__main__':
	t = int(raw_input())
	for _ in xrange(t):
		n = int(raw_input())
		gpa = map(float, raw_input().split())
		
		corr, best = 0, 0
		for i in xrange(5):
			temp = map(float, raw_input().split())
			current = pearson(gpa, temp, n)
			if corr < current:
				corr, best = current, i+1
		print best
		