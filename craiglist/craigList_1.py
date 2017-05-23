import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

def feature(parsed):
    return (parsed['city'] + ' ')*2 + (parsed['section'] + ' ')*7 + parsed['heading']

train = open('training.json', 'r')
N = int(train.readline())
X = [None] * N
y = [None] * N
for i in range(N):
    parsed = json.loads(train.readline().lower())
    X[i] = feature(parsed)
    y[i] = parsed['category']
train.close()
print y[0:10]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

tfidf = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
clf = LinearSVC(C=1.1)
pipeline = Pipeline([('prep', tfidf), ('clf', clf)])
print X[0:10]
pipeline.fit(X_train, y_train)
pipeline.predict(X_test)
print pipeline.score(X_test, y_test)

n = 6
x_test = []
test = ['{"city":"chicago","section":"for-sale","heading":"Madden NFL 25 XBOX 360. Brand New!"}','{"city":"paris.en","section":"housing","heading":" looking for room to rent."}','{"city":"newyork","section":"for-sale","heading":"two DS game"}','{"city":"seattle","section":"housing","heading":"map"}','{"city":"singapore","section":"services","heading":"Good Looking Asian Sensation N aughty Girl ---- Independent"}','{"city":"newyork","section":"for-sale","heading":"map"}']
for i in xrange(n):
	#a = '{"city":"chicago","section":"for-sale","heading":"Madden NFL 25 XBOX 360. Brand New!"}'
	temp = json.loads(unicode(test[i].lower(),'utf8'))
	x_test.append(feature(temp))
print '\n'.join(clf.predict(x_test))
