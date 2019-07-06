import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


def equalize_hist(original_image):

    original_image = cv2.imread(original_image, cv2.IMREAD_GRAYSCALE)

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)
    total_number_of_pixels = height * width

    f = [0] * 256
    new_gray_level = [0] * 256

    for i in range(height):
        for j in range(width):
            f[original_image[i][j]] = f[original_image[i][j]] + 1

    curr = 0

    for i in range(256):
        curr = curr + f[i]

        new_gray_level[i] = round((curr * 255) / total_number_of_pixels)

    cv2.imshow('original image', original_image)

    for i in range(height):
        for j in range(width):
            original_image[i][j] = new_gray_level[original_image[i][j]]

    cv2.imshow('after image histogram equalization', original_image)
    plt.figure('after image histogram equalization')
    plt.plot(new_gray_level)
    plt.figure('original image')
    plt.plot(f)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    org_image = str(sys.argv[1])
    equalize_hist(org_image)
