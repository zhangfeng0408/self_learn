#!/usr/bin/env python
#coding
import numpy as np 
import cv2
refPt=[]
def draw_circle(event,x,y,flags,param):
	if event==cv2.EVENT_MOUSEMOVE:
		cv2.circle(img,(x,y),100,(0,0,255),-1)
		cv2.imshow('image',img)
def click_and_cropping(event,x,y,flags,param):
	global refPt,img
	if event==cv2.EVENT_LBUTTONDOWN:
		refPt=[(x,y)]
	elif event==cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		cv2.rectangle(img,refPt[0],refPt[1],(0,255,0),2)
		cv2.imshow('image',img)
img=cv2.imread('digit.png')
clone=img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_and_cropping)

while True:
	cv2.imshow('image',img)
	k=cv2.waitKey(0)&0xFF
	if k==27:
		break
		cv2.destroyAllWindows()
	elif k==ord('r'):
		img=clone.copy()
	elif k==ord('c'):
		cv2.namedWindow('ROI')
		roi=clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
		cv2.imshow('ROI',roi)
	elif k==ord('s'):
		cv2.imwrite('image.jpg',img)
		cv2.destroyAllWindows()
		break
