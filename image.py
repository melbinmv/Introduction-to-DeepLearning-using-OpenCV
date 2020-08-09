import numpy as np
import cv2
img = cv2.imread('bcon.jpg')
#print(type(img)
#print(img.shape)B G and R
b = img[:,:,0]#Row,Column,Channel
print(b)
g = img[:,:,1]
r = img[:,:,2]
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red', r)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
