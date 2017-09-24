#!/usr/bin/env pythons
#coding:utf-8
import numpy as np 
import cv2

# img=cv2.imread('messi5.jpg',0)
img=cv2.imread('messi5.jpg',1)
print img
cv2.imshow('image',img)
k=cv2.waitKey(0)&0xFF
if k==27:
	cv2.destroyAllWindows()
elif k==ord('c'):
	cv2.putText(img,'HelloWorld',(100,300),2,5,(0,0,255),2)
	cv2.imwrite('messigray_putText.png',img)
	cv2.destroyAllWindows()
elif k==ord('s'):
	cv2.imwrite('messigray.png',img)
	cv2.destroyAllWindows()