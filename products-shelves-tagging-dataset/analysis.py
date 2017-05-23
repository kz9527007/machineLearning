# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, BaggingRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import nltk
from nltk.corpus import stopwords
import re
import time

stemmer = nltk.stem.snowball.SnowballStemmer('english')
porter = nltk.PorterStemmer()
#nltk.download()

def str_stemmer(s):
	#print s
	return " ".join([stemmer.stem(word) for word in s.split()])

def str_common_word(x, y):
	return sum(int(y.find(word)>=0) for word in x.split())
	
def remover(x):
	#print x
	x = re.sub('<[^>]+>', ' ', x)
	x = x.replace('&',' ').replace('\\',' ')
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
		#stop = set(stopwords.words('english'))
		stop = ['a','about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves','com']
		#print t
		t = ' '.join([i for i in t.split(' ') if i not in stop])
	return t

def num(x):
	if not str(x).isdigit():
		#print x
		x = ord(x)
	return x
	
def main():
	start = time.time()
	df_train = pd.read_csv('train.tsv', encoding="utf-8", sep='\t', header=0)
	df_test = pd.read_csv('test.tsv', encoding="utf-8", sep='\t', header=0)
	
	# Initial Analysis
	t = df_train.shape[0]
	df = pd.concat((df_train, df_test), axis=0, ignore_index=True)
	l = list(df_train.columns.values)
	print df_train.shape[0], df_test.shape[0]
	for i in l:
		print i, df_train[i].isnull().sum(), df_test[i].isnull().sum()
	
	
	print time.time() - start
if __name__ == '__main__':
	main()