#!/usr/bin/env python
#coding:utf-8
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.decomposition import PCA
from sklearn.cross_validation import cross_val_score,StratifiedKFold


iris=load_iris()
X,y=iris.data,iris.target
#print X,y
X_train,X_test,y_train,y_test=train_test_split(X,y)
# print X_train,y_train

clf=SVC()
clf.fit(X_train,y_train)
joblib.dump(clf,'iris.pk')
y_pred=clf.predict(X_test)

pca=PCA(n_components=2)
pca.fit(X)
X_pca=pca.transform(X)

scores=cross_val_score(SVC(),X_train,y_train,cv=5)
print scores

