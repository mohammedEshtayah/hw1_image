import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


original_image = cv2.imread('Fig0305(a)(DFT_no_log).tif').astype(np.uint8)




def log_transformation():

    out = cv2.normalize(original_image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)

    factor = 5

    cv2.imshow('original image', original_image)

    print(height)
    print(width)

    for i in range(height):
        for j in range(width):
            out[i][j] = factor * np.log((1 + out[i, j]))


    cv2.imshow('new image', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def power_transformation():
    y = 1
    c = 1
    cv2.imshow('image', c * np.power(original_image, y))
    cv2.waitKey(0)


def calc_histogram():
    histogram = cv2.calcHist([original_image], [0], None, [256], [0, 256])
    plt.plot(histogram)
    plt.show()


def equalize_hist():
    img = cv2.imread('Fig0308(a)(fractured_spine).tif')
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow('Histogram equalized', img_output)
    cv2.waitKey(0)


def main():
    log_transformation()
    power_transformation()
    calc_histogram()
    equalize_hist()


if __name__ == "__main__": main()
