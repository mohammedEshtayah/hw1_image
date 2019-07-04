import cv2  
import numpy as np;
import math
im=cv2.imread('3(a).tif',0)
 #print('{}'.format(a.shape[0])

cv2.imshow('image',im)
cv2.waitKey(0)

cv2.destroyAllWindows()
def  log_transformation():

    im1=cv2.threshold(np.uint8(np.log1p(im)),1,255,cv2.cv2.THRESH_BINARY)[1]
    cv2.imshow('image',im1)
    cv2.waitKey(0)
def  power_transformation():
    #im=cr^y
    cv2.imshow('image',1* np.power(im,1))
    cv2.waitKey(0)

def main():
    #log_transformation()
    power_transformation()
    print("fac")
    print("aaa")
    #print(im[45][80])
    #item[]
    #for i in range(0, 10):
    #    for j in range(0,10):
    #        item[i][j]=image[i][j]

    #cv2.imshow('image',item)
    #print("new {}".format(im[1]))
 


if __name__ == "__main__":main()
