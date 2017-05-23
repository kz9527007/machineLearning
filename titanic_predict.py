import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def benchmark(clf, x_test, y_test):
	clf.fit(x_test,y_test)
	#pred_test = clf.predict(X_test)
	
	pred_actual = clf.predict(x_test)
	#print pred_actual, len(pred_actual)
	y_test = y_test.as_matrix()
	wrong = sum([pred_actual[i] != y_test[i] for i in xrange(len(y_test))])
	return wrong

def randomForest(X_train, X_test, y_train, y_test):
	clf = RandomForestClassifier(n_estimators=10)
	clf.fit(X_train,y_train)
	wrong = benchmark(clf, X_test, y_test)
	print 'randomForest = ' + str(wrong)
	return clf, wrong
	
def logistic(X_train, X_test, y_train, y_test):	#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
	clf = LogisticRegression()
	clf.fit(X_train,y_train)
	wrong = benchmark(clf, X_test, y_test)
	print 'logistic = ' + str(wrong)
	return clf, wrong
	
def decisionTree(X_train, X_test, y_train, y_test):
	clf = DecisionTreeClassifier()
	clf.fit(X_train,y_train)
	wrong = benchmark(clf, X_test, y_test)
	print 'decisionTree = ' + str(wrong)
	return clf, wrong

def supportVector(X_train, X_test, y_train, y_test):
	clf = svm.SVC()
	clf.fit(X_train,y_train)
	wrong = benchmark(clf, X_test, y_test)
	print 'svm = ' + str(wrong)
	return clf, wrong

def modelFinder(X_train, X_test, y_train, y_test):
	clf1, result1 = logistic(X_train, X_test, y_train, y_test)
	clf2, result2 = decisionTree(X_train, X_test, y_train, y_test)
	clf3, result3 = supportVector(X_train, X_test, y_train, y_test)
	clf4, result4 = randomForest(X_train, X_test, y_train, y_test)
	
	result = [result1, result2, result3, result4]
	if min(result) == result1:
		return clf1
	elif min(result) == result2:
		return clf2
	elif min(result) == result3:
		return clf3
	elif min(result) == result4:
		return clf4
		
def preprocessing(X):
	# Need to modify the raw data for modeling
	# All missing Embarked -> just make them embark from most common place
	if len(X.Embarked[ X.Embarked.isnull() ]) > 0:
		X.Embarked[ X.Embarked.isnull() ] = X.Embarked.dropna().mode().values
	Ports = list(enumerate(np.unique(X['Embarked'])))    # determine all values of Embarked,
	Ports_dict = { name : i for i, name in Ports }              # set up a dictionary in the form  Ports : index
	X.Embarked = X.Embarked.map( lambda x: Ports_dict[x]).astype(int)     # Convert all Embark strings to int
	
	# Classify people by prefix of passenger name
	X['Group'] = ''
	for i in range(1, len(X)):
		name = X.Name.irow(i)
		if 'Mr' in name:
			X['Group'].iloc[i] = 'Mr'
		elif 'Miss' in name:
			X['Group'].iloc[i] = 'Miss'
		elif 'Mrs' in name:
			X['Group'].iloc[i] = 'Mrs'
		elif 'Master' in name:
			X['Group'].iloc[i] = 'Master'
		elif 'Dr' in name:
			X['Group'].iloc[i] = 'Dr'
		else:
			X['Group'].iloc[i] = 'Other'
	
	mr_age = all_[all_['Group'] == 'Mr']['Age'].dropna().mean()
	mrs_age = all_[all_['Group'] == 'Mrs']['Age'].dropna().mean()
	miss_age = all_[all_['Group'] == 'Miss']['Age'].dropna().mean()
	master_age = all_[all_['Group'] == 'Master']['Age'].dropna().mean()
	dr_age = all_[all_['Group'] == 'Dr']['Age'].dropna().mean()
	other_age = all_[all_['Group'] == 'Other']['Age'].dropna().mean()
	
	for i in range(1, len(X)):
		if X['Group'].iloc[i] == 'Mr':
			X['Age'].iloc[i] = mr_age
		elif X['Group'].iloc[i] == 'Mrs':
			X['Age'].iloc[i] = mrs_age
		elif X['Group'].iloc[i] == 'Miss':
			X['Age'].iloc[i] = miss_age
		elif X['Group'].iloc[i] == 'Master':
			X['Age'].iloc[i] = master_age
		elif X['Group'].iloc[i] == 'Dr':
			X['Age'].iloc[i] = dr_age
		elif X['Group'].iloc[i] == 'Other':
			X['Age'].iloc[i] = other_age
	
	X['Gender'] = X['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
	return X

def dataExploration(X,y,columns):
	print 'Number of nan values per column'
	for i in columns:
		print i, X[i].isnull().sum()
	# dropping "Cabin" due to too many nan values
	
	print '--------------------------------------------------------------'
	print 'Number of Gender by Survived'
	print (X['Sex'] == 'male') == (y == 1)
	print 'Survived male = ', X[(X['Sex'] == 'male') == (y == 1)]['Sex'].count()
	print 'Survived female = ', X[(X['Sex'] == 'female') == (y == 1)]['Sex'].count()
	print 'Not survived male = ', X[(X['Sex'] == 'male') == (y == 0)]['Sex'].count()
	print 'Not survived male = ', X[(X['Sex'] == 'female') == (y == 0)]['Sex'].count()
	
	print '--------------------------------------------------------------'
	print 'Number of Age'
	#print X[y==1]['Age'].dropna().astype(int).as_matrix()
	plt.subplot(2, 1, 1)
	plt.hist(X[y==1]['Age'].dropna().astype(int).as_matrix())
	plt.title('Age distribution of survival')
	plt.subplot(2, 1, 2)
	plt.hist(X[y==0]['Age'].dropna().astype(int).as_matrix())
	plt.title('Age distribution of non-survival')
	plt.show()

	a = raw_input('a')
if __name__ == "__main__":
	fid = pd.read_csv('train.csv', header=0)
	X = fid[['Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']]
	y = fid['Survived']
	
	dataExploration(X,y,['Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'])
	
	X = preprocessing(X)
	
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
	
	columns =['Pclass','Gender','SibSp','Parch','Fare','Embarked']
	# Which columns to use?
	X_train = X_train[columns]
	X_test = X_test[columns]
	
	print X_train[y_train == 1].describe()
	print X_train[y_train == 0].describe()
	
	clf = modelFinder(X_train, X_test, y_train, y_test)
	
	test = pd.read_csv('test.csv', header=0)
	x_test = test[['Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']]
	
	x_test = preprocessing(x_test.fillna(0))
	x_test = x_test[columns]

	y_test = clf.predict(x_test)
	
	df = test['PassengerId'].as_matrix()
	dataSet = list(zip(df,y_test))
	df = pd.DataFrame(data = dataSet, columns=['PassengerId', 'Survived'])
	df.to_csv('result_SuBae.csv',index=False,header=True)