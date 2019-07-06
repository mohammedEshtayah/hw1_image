import cv2
import sys
import numpy as np


def arithmetic_operations(first_image, second_image, operation):

    first_image = cv2.imread(first_image)
    second_image = cv2.imread(second_image)

    first_image_height = np.size(first_image, 0)
    first_image_width = np.size(first_image, 1)

    second_image_height = np.size(second_image, 0)
    second_image_width = np.size(second_image, 1)

    if (first_image_height != second_image_height) or (first_image_width != second_image_width):
        print("you should enter two images with the same size to do arithmetic operations !")
        return

    else:

        if operation == 'plus' or operation == 'Plus' or operation == 'sum' or operation == 'Sum' or operation == '+':

            final_image = first_image + second_image

            cv2.imshow('first image', first_image)
            cv2.imshow('second image', second_image)
            cv2.imshow('after done arithmetic operation', final_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif operation == 'minus' or operation == 'Minus' or operation == '-':

            final_image = first_image - second_image

            cv2.imshow('first image', first_image)
            cv2.imshow('second image', second_image)
            cv2.imshow('after done arithmetic operation', final_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            print("invalid operation")
            return


if __name__ == "__main__":

    fir_img = str(sys.argv[1])
    sec_img = str(sys.argv[2])

    op = str(sys.argv[3])

    arithmetic_operations(fir_img, sec_img, op)
