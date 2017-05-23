import numpy as np

fid = open('input.txt')

f,n = map(int, fid.readline().split(' '))

X,y = [],[]
for i in xrange(n):
	temp = map(float, fid.readline().split(' '))
	X.append(temp[0:f] + [1])
	y.append(temp[-1])

m = np.linalg.lstsq(np.array(X), np.array(y))[0]
print m
nn = int(fid.readline())

for j in xrange(nn):
	temp = map(float, fid.readline().split(' ')) + [1]
	output = np.dot(np.array(temp),m)
	print output
	