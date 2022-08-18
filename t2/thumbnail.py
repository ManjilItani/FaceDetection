#! /usr/bin/python

import cv2
import glob
import os

bodyCascade = cv2.CascadeClassifier('data/haarcascade_mcs_upperbody.xml')
faceCascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')
frame = cv2.imread('input.png')
frameHeight, frameWidth, frameChannels = frame.shape

regions = bodyCascade.detectMultiScale(frame, 1.5, 1)
x,y,w,h = regions[0]
cv2.imwrite('thumbnail.png', frame[0:frameHeight,x:x+w])
cv2.rectangle(frame,(x,0),(x+w,frameHeight),(0,255,255),6)

faceregions = faceCascade.detectMultiScale(frame, 1.5, 2)
x,y,w,h = faceregions[0]
cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)

# cv2.imshow("Result",frame)
# cv2.waitKey(0)
cv2.imwrite('out.png', frame)