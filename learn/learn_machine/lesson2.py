#!/usr/bin/env python
#coding:utf-8
from sklearn.datasets import load_iris
#from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

iris=load_iris()
X,y=iris.data,iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y)

clf=RandomForestClassifier()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
scores=clf.score(X_test,y_test)
print scores
print y_pred