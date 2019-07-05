import cv2
import sys
import numpy as np


def log_transformation(original_image, factor):

    original_image = cv2.imread(original_image).astype(np.uint8)
    out = cv2.normalize(original_image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

    height = np.size(original_image, 0)
    width = np.size(original_image, 1)

    cv2.imshow('original image', original_image)

    for i in range(height):
        for j in range(width):
            out[i][j] = factor * np.log((1 + out[i, j]))

    cv2.imshow('new image', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    log_transformation()


if __name__ == "__main__":
    org_image = str(sys.argv[1])
    f = int(sys.argv[2])
    log_transformation(org_image, f)
