#!/usr/bin/env python
#coding:utf-8
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
img=cv2.imread('digit1.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print gray
# print gray.shape
#cv2.namedWindow('gray')
cv2.imshow('image',img)
# k=cv2.waitKey(0)&0xFF
# if k==27:
# 	cv2.destroyAllWindows()
# plt.imshow(gray)
# plt.show()
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)] 
print np.hsplit(gray,100)
print 'Make it into a Numpy array. It size will be (50,100,20,20)'  
x = np.array (cells)  
print x.shape  
print 'train data.........'  
train = x[:,:50].reshape(-1,400).astype(np.float32)  
print train.shape  
test = x[:,50:100].reshape(-1,400).astype(np.float32)  
print test.shape  
  
print 'create labels for train and test data'  
k = np.arange(10)  
print k  
#print np.repeat(k,250).reshape(2500,1)  
train_labels = np.repeat(k,250)[:,np.newaxis]  
test_labels = train_labels.copy()  
print train_labels.shape  
print test_labels.shape  
  
print 'Initiate knn,train data'  
knn = cv2.KNearest()  
knn.train(train,train_labels)  
print 'then test it with test data for k = 5'  
ret,result,neigobours,dist = knn.find_nearest(test,k = 5)  
  
print 'check the accuracy of classification'  
matches = result == test_labels  
correct = np.count_nonzero(matches)  
accuracy = correct*100/result.size  
print accuracy,