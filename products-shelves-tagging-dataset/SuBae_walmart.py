# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, BaggingRegressor, AdaBoostClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
import nltk
from nltk.corpus import stopwords
import re
import time

stemmer = nltk.stem.snowball.SnowballStemmer('english')
porter = nltk.PorterStemmer()
#nltk.download('all')

def str_stemmer(s):
	#print s
	return " ".join([stemmer.stem(word) for word in s.split()])

def str_common_word(x, y):
	return sum(int(y.find(word)>=0) for word in x.split())
	
def remover(x):
	#print x
	x = re.sub('<[^>]+>', ' ', x)
	x = x.replace('&','').replace('\\','')
	x = x.replace('.com','')
	u = ''
	for i in x:
		if i == ' ' or i.isalpha() or i.isdigit():
			u += i.lower()
		else:
			u += ' '
	t = ' '.join(u.split())
	if t == '':
		t = ''
	else:
		stop = set(stopwords.words('english'))
		#stop = ['a','about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves','com']
		#print t
		t = ' '.join([i for i in t.split(' ') if i not in stop and len(i) > 2])
	return t

def num(x):
	if not str(x).isdigit():
		#print x
		x = ord(x)
	x = str(x)*5
	return x
	
def main():
	start = time.time()
	df_train = pd.read_csv('train.tsv', encoding="utf-8", sep='\t', header=0)
	df_test = pd.read_csv('test.tsv', encoding="utf-8", sep='\t', header=0)
	
	# Initial Analysis
	
	
	t = df_train.shape[0]
	df = pd.concat((df_train, df_test), axis=0, ignore_index=True)
	l = list(df_train.columns.values)
	
	# Columns to use
	c = ["Seller","Product Long Description","Product Name","Short Description","Actual Color"]
	#c = ["Product Long Description","Product Name"]
	d = ["tag"]
	
	for j,i in enumerate(df["Item Class ID"].values):
		if not str(i).isdigit():
			print df["item_id"].iloc[j],i,j
	
	for i in c:
		df[i].fillna('', inplace=True)
		df[i] = df[i].map(lambda x:remover(x))
		df[i] = df[i].map(lambda x:str_stemmer(x))
	
	# Change data type to numeric
	df["Item Class ID"].fillna(0, inplace=True)
	df["Item Class ID"] = df["Item Class ID"].map(lambda x:num(x))
	#df[["Item Class ID"]] = df[["Item Class ID"]].astype(np.int64)
	
	#df_train['seller'] = df_train['Seller'].map(lambda x:str_common_word(x))
	#df_train['title'] = df_train['Product Name'].map(lambda x:str_common_word(x))
	#df_train['description'] = df_train['Product Long Description'].map(lambda x:str_common_word(x))
	n1,n2,n3,n4 = 1,4,5,0
	df['all'] = (df['Seller'] + ' ')*n1 + (df['Product Name'] + ' ')*n2 + (df['Item Class ID'] + ' ')*n3 + (df['Short Description'] + ' ')*n4 + df['Product Long Description']
	#df['all'] = (df['Seller'] + ' ')*n1 + (df['Product Name'] + ' ')*n2 + (df['Item Class ID'] + ' ')*n3 + (df['Short Description'] + ' ')*n4 + df['Product Long Description'] + ' ' + df['Actual Color']
	#df['all'] = (df['Product Name'] + ' ')*n2 + (df['Short Description'] + ' ')*n4
	print df['all'].iloc[:2].values
	
	df_train = df.iloc[:t]
	df_test = df.iloc[t:]
	
	y = df_train['tag'].values
	y_n = len(list(set(y)))
	#x = df_train[['Seller','Product Name','Product Long Description']].values
	x_train = df_train['all'].values
	x_test = df_test['all'].values
	x_v = df_train['Item Class ID'].values
	
	clf = LinearSVC(C=1.5)
	#clf = DecisionTreeClassifier(max_features='int')
	#clf = RandomForestClassifier(n_estimators=30)
	#clf = BaggingRegressor(rf, n_estimators=20, max_samples=0.1, random_state=25)
	vectorizer = TfidfVectorizer(max_df=0.4,ngram_range=(0,1),sublinear_tf=True, stop_words='english')
	#vectorizer = TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True, stop_words='english')
	X_train = vectorizer.fit_transform(x_train)
	X_test = vectorizer.transform(x_test)
	
	clf.fit(X_train,y)
	print clf.score(X_train,y)
	
	y_pred = clf.predict(X_test)
	print '-----------------------'
	a = df_test['item_id'].values
	output = open('tags.tsv','wb')
	output.write('item_id'+'\t'+'tag'+'\r\n')
	for i in xrange(len(y_pred)):
		output.write(str(a[i])+'\t'+y_pred[i]+'\r\n')
	print time.time() - start
if __name__ == '__main__':
	main()