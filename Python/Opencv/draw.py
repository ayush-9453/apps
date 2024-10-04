import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

img = cv.imread('Photo/cat.jpg')
cv.imshow('Cat',img)

# point the image a certain colour
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green',blank)

# draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,250,0),thickness= -1)
cv.imshow('Rectangle',blank)

# Draw a circle 
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=3)
cv.imshow('circle',blank)

# Draw a line
cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness= 3)
cv.imshow('line',blank)

# Write a text on image
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text', blank)

cv.waitKey(0)