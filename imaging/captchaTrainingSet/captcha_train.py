from sklearn.naive_bayes import BernoulliNB
from numpy import array, empty
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib
def scale(x):
	r,g,b = map(int, x.split(','))
	output = 1
	if r + g + b > 400:
		output = 0
	return output

inputFiles = [f for f in listdir('inputTraining') if isfile(join('inputTraining',f))]
outputFiles = [f for f in listdir('outputTraining') if isfile(join('outputTraining',f))]

train = []
y = []
for input, output in zip(inputFiles, outputFiles):
	print input, output
	fid = open('inputTraining/'+input)
	answer = open('outputTraining/'+output)
	for k in answer.readline().replace('\r\n','').replace('\n',''):
		y += [k]
	r,c = map(int,fid.readline().split())
	data_temp = empty([r,c])
	#output = open('temp.txt','wb')
	for i in xrange(r):
		t = fid.readline().split()
		temp = [scale(x) for x in t]
		data_temp[i] = temp
	outputFid = open('temp.txt','wb')
	ar = []
	for i in xrange(5):
		ar.append(data_temp[:,34*i:34*(i+1)].flatten())
		temp = data_temp[:,34*i:34*(i+1)].flatten()
		train.append(temp)

out1 = open('train.txt','wb')
out2 = open('y.txt','wb')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = {}
yy = []
for letter in alphabet:
	counter[letter] = 0
for jj, ii in enumerate(train):
	current = y[jj]
	if counter[y[jj]] < 4:
		out1.write(''.join([str(int(x)) for x in ii])+',')
		yy.append(y[jj])
		counter[y[jj]] += 1
out2.write(str(yy))

		
clf = BernoulliNB()
clf.fit(train, y)
joblib.dump(clf, 'test.pkl',compress=9)
joblib.dump(clf, 'test1.pkl')
prediction = clf.predict(train)
print reduce(lambda a,b:a+b, prediction)
print y
print len(prediction), len(y)