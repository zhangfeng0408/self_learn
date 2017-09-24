#!/usr/bin/env python
#coding:utf-8
import random
def create_num(num):
	list=['131','132','133','135','135','137','138','139','151','152','153','155','156','158','159','176','177','181','182','183','185','186','187','188','189']
	str='0123456789'
	f=open('phonenumber.txt','ab')
	resultlist=[]
	for i in range(num):
		result=random.choice(list)+''.join(random.choice(str) for i in range(8))
		print result
		resultlist.append(result)
	resulttouple=tuple(resultlist)
	for result in resulttouple:
		f.writelines(result+'\n')
		f.flush()
	f.close()
create_num(10000000)