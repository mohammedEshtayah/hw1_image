import cv2
import numpy as np
from matplotlib import pyplot as plt


original_image = cv2.imread('Fig0308(a)(fractured_spine).tif', 0)


def calc_histogram():

#    histogram = cv2.calcHist([original_image], [0], None, [256], [0, 256])

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)

    f = [0] * 256

    for i in range(height):
        for j in range(width):
            f[original_image[i][j]] = f[original_image[i][j]] + 1
    plt.figure()
    plt.plot(f)
    plt.show()


def equalize_hist():
    img = cv2.imread('Fig0308(a)(fractured_spine).tif')
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow('Histogram equalized', img_output)
    cv2.waitKey(0)


def main():

    calc_histogram()
    equalize_hist()


if __name__ == "__main__": main()
