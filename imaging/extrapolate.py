
def extrapolate(r,c,n,r_r,c_r,ar):
	output = []
	for i in xrange(r):
		temp = []
		for j in xrange(c):
			temp.append(ar[i][j])
			for k in xrange(n-1):
				if len(temp) == c_r:
					break
				if len(temp) >= j+1:
					temp.append(ar[i][j])
				else:
					#print i,j,len(temp), c*n
					temp.append(tuple([sum(x)/n*(k+1) for x in zip(ar[i][j],ar[i][j+1])]))
		output.append(temp)
		for l in xrange(n-1):
			if len(output) == r_r:
				break
			if len(output) >= i+1:
				temp = output[-1]
			else:
				line = []
				for kk in xrange(c):
					line.append(tuple([sum(x)/n*(l+1) for x in zip(ar[i][kk],ar[i+1][kk])]))
				
				#print line
				temp = []
				for jj in xrange(c):
					temp.append(line[jj])
					for kk in xrange(n-1):
						if len(temp) == c_r:
							break
						if len(temp) >= jj+1:
							temp.append(line[jj])
						else:
							#print i,j,len(temp), c*n
							temp.append(tuple([sum(x)/n*(kk+1) for x in zip(line[jj],line[jj+1])]))
			output.append(temp)
	for row in output:
		print ' '.join([str(item).replace(' ','').replace('(','').replace(')','') for item in row])


if __name__ == '__main__':
	'''
	r,c,n = map(int,raw_input().split())
	r_r,c_r = map(int, raw_input().split())
	ar = []
	for _ in xrange(r):
		ar.append(map(tuple, [map(int,y.split(',')) for y in raw_input().split()]))
	print ar
	print '------------'
	'''
	fid = open('input.txt')
	r,c,n = map(int, fid.readline().split())
	r_r,c_r = map(int, fid.readline().split())
	ar = []
	for _ in xrange(r):
		ar.append(map(tuple, [map(int,y.split(',')) for y in fid.readline().split()]))
	#print ar
	extrapolate(r,c,n,r_r,c_r,ar)