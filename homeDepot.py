import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

def remover(x):
	remove = ['a','the','an','when','this','that','these','on','in','by','what','which','those','why','from','and','but','for','also','39;','amp;']
	return " ".join([word for word in x.lower().split() if word.strip() not in remove])

def special(x):
	special_character1 = '!@#$%^&+=().,-'
	for i in special_character1:
		x = x.replace(i,'')
	special_character2 = '*-'
	for j in special_character2:
		x = x.replace(j,' ')
	return " ".join([word for word in x.lower().split()])
	
def special_search(x):
	special_character = '*'
	for i in special_character:
		x = x.replace(i,'x')
	return " ".join([word for word in x.lower().split()])
	
def preprocessing(df_train, description):
	# Remove unnecessary terms from descriptions + lower case
	description['product_description'] = description['product_description'].map(lambda x: remover(x))
	df_train['search_term'] = df_train['search_term'].map(lambda x: remover(x))
	df_train['product_title'] = df_train['product_title'].map(lambda x: remover(x))
	# Modify dimension
	#description['product_description'] = description['product_description'].amp(lambda x: dimension(x))
	
	# Lower Case + replace x and * with whitespace
	df_train['search_term'] = df_train['search_term'].map(lambda x: special_search(x))
	description['product_description'] = description['product_description'].map(lambda x: special_search(x))
	# Lower Case + replace special characters with whitespace
	df_train['product_title'] = df_train['product_title'].map(lambda x: special(x))
	
	# Cleansing
	description['product_description'] = description['product_description'].map(lambda x: cleansing(x))
	df_train['product_title'] = df_train['product_title'].map(lambda x: cleansing(x))
	df_train['search_term'] = df_train['search_term'].map(lambda x: cleansing(x))
	return df_train, description

def vectorizer(x,y):
	#vectorizer = TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)
	
	#clf = PassiveAggressiveClassifier(n_iter=100)
	#clf = MultinomialNB(alpha=0.05)
	#clf = LinearSVC(C=1.5)
	clf = RandomForestClassifier(n_estimators=10)
	
	#pipeline = Pipeline([('prep', vectorizer), ('clf', clf)])
	
	clf.fit(x, y)
	#clf.fit(X_train, y_train)
	#print pipeline.score(X_test,y_test)
	return clf
	
def cleansing(x):
	units = [('\'','in'), (' in D x ','x'), (' in H x ','x'), (' ft D x ','x'), (' ft H x ','x'), (' in x ','x'), (' ft x ','x')]
	for i in units:
		for j in xrange(len(x)):
			x[j] = x[j].replace(i[0],i[1])
	return x
	
def pointConverter(x1, x2):
	return len([xx for xx in x2[i].split(' ') if xx in x1[i]]))
	
def main():
	#df_train, df_test = readFile()
	df_train = pd.read_csv('train.csv', encoding="ISO-8859-1", dtype={'relevance':np.float64})
	df_test = pd.read_csv('test.csv', encoding="ISO-8859-1")
	description = pd.read_csv('product_descriptions.csv', encoding="ISO-8859-1")
	
	train_num = df_train.shape[0]
	
	df_combine = pd.concat((df_train,df_test), axis=0, ignore_index=True)
	print 'Reading CSV files complete'
	
	df_combine, description = preprocessing(df_combine, description)
	print 'Preprocessing complete'
	
	df_combine = pd.merge(df_combine, description, how='left', on='product_udi')

	# Point Converter
	df_combine['word_in_title'] = df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[1]))
	df_combine['word_in_description'] = df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[2]))
	# Cross-validation
	xx, xt, yy, yt = train_test_split(x, y_train, test_size=0.3, random_state=42)
	clf_cv = vectorizer(xx, yy)
	print clf_cv.score(xt, yt)
	print 'Cross-validation complete'
	
	clf = vectorizer(x_train, y_train)
	print 'Actual fitting complete using LinearSVC'
if __name__ == "__main__":
	main()