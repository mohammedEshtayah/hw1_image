import cv2
import sys
import numpy as np


def power_transformation(original_image, factor, power):

    original_image = cv2.imread(original_image).astype(np.uint8)
    out = cv2.normalize(original_image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)

    for i in range(height):
        for j in range(width):
            out[i][j] = factor * np.power(out[i, j], power)

    cv2.imshow('original image', original_image)
    cv2.imshow('after apply power transformation', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    org_image = str(sys.argv[1])
    f = int(sys.argv[2])
    p = float(sys.argv[3])
    power_transformation(org_image, f, p)
