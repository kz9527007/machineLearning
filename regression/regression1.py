import sys
import itertools
import numpy as np

def powerCalculate(x,p):
	output = 1
	for index, value in enumerate(p):
		output *= x[index]**value
	return output

def modify(X,powers):
	output = []
	print 'X', X
	for i in X:
		temp = []
		for power in powers:
			print i, power, powerCalculate(i,power)
			temp.append(powerCalculate(i,power))
		output.append(temp)
	print output
	a = raw_input('a')
	return output

def gradientDescent(Theta,X,Y,threshold,alpha):
	# Obtained the equation from http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex3/ex3.html
	merge = 10
	while merge >= alpha:
		Theta_new = Theta - np.array([alpha/len(X)*np.sum((X.dot(Theta) - Y.T)*X,axis=0)]).T
		merge = np.max(np.abs(Theta_new - Theta))
		Theta = Theta_new
	return Theta, merge

fid = open('input.txt')
f,m = map(int, fid.readline().split(' '))
X = []
Y = []
alpha, threshold, Theta = 0.1, 0.001, [0.0]*(f+1)

for i in xrange(m):
  temp = map(float, fid.readline().split(' '))
  X.append(temp[0:f])
  Y.append(temp[-1])
Y = np.array([Y])

X_test = []
t = int(fid.readline())
for i in xrange(t):
	temp = map(float, fid.readline().split(' '))
	X_test.append(temp)

# Assign the polynomial degree you are interested
order = 3

best = 0
Theta_best = []
degree = 0
for j in xrange(2,order):
	powers = [x for x in itertools.product(range(j),repeat=f) if sum(x) < j]
	print j, powers
	X_current = np.array(modify(X,powers))
	Theta = np.array([[0.0]]*len(powers))
	Theta, merge = gradientDescent(Theta,X_current,Y,threshold,alpha)
	if merge > best:
		best, degree = merge, j
		Theta_best = Theta

degree = 4
powers = [x for x in itertools.product(range(degree),repeat=f) if sum(x) < degree]
X_test = np.array(modify(X_test,powers))
output = X_test.dot(Theta)
for i in output:
	print i[0]