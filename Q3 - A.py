import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


def calc_histogram(original_image):

    original_image = cv2.imread(original_image, 0)

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)

    f = [0] * 256

    for i in range(height):
        for j in range(width):
            f[original_image[i][j]] = f[original_image[i][j]] + 1

    plt.figure()
    plt.plot(f)
    plt.show()


if __name__ == "__main__":
    org_image = str(sys.argv[1])
    calc_histogram(org_image)
