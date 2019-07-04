import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('Fig0308(a)(fractured_spine).tif')

cv2.waitKey(0)

cv2.destroyAllWindows()


def log_transformation():
    # im1 = cv2.threshold(np.uint8(np.log1p(im)), 1, 255, cv2.cv2.THRESH_BINARY)[1]
    # cv2.imshow('image', im1)

    iml = np.uint8(np.log1p(im))

    threshold = 1

    img_2 = cv2.threshold(iml, threshold, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow('original image', im)
    cv2.imshow('after log transformed', img_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def power_transformation():
    y = 1
    c = 1
    cv2.imshow('image', c * np.power(im, y))
    cv2.waitKey(0)


def calc_histogram():
    histogram = cv2.calcHist([im], [0], None, [256], [0, 256])
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
