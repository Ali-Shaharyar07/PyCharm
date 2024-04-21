import cv2
import numpy as np

img = cv2.imread("shapeds.png")
img1 =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY_INV)

cnts, hier = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(cnts, " Number of Contour \n", len(cnts), "Total Contours\n", hier, " Heirarchy")