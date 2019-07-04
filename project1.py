import cv2  
import numpy as np;
import math
from matplotlib import pyplot as plt 
im=cv2.imread('3(a).tif',0)
#print('{}'.format(a.shape[0])

#cv2.imshow('image',im)
cv2.waitKey(0)

cv2.destroyAllWindows()
def  log_transformation():

    im1=cv2.threshold(np.uint8(np.log1p(im)),1,255,cv2.cv2.THRESH_BINARY)[1]
    cv2.imshow('image',im1)
    cv2.waitKey(0)
def  power_transformation():
    #im=cr^y
    y=1
    c=1
    cv2.imshow('image',c* np.power(im,y))
    cv2.waitKey(0)
def calc_Histogram():
    histr = cv2.calcHist([im],[0],None,[256],[0,256]) 
    plt.plot(histr) 
    plt.show()  
def equalize_Hist():
    img = cv2.imread('3(a).tif')
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow('Histogram equalized', img_output)

    cv2.waitKey(0)   
def main():
    #log_transformation()
    #power_transformation()
    #calc_Histogram() 
    equalize_Hist()
  
 


if __name__ == "__main__":main()
