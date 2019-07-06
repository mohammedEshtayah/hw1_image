import cv2
import sys



def arithmetic_operations(image, value, operation):

    image = cv2.imread(image)

    if operation == 'plus' or operation == 'Plus' or operation == 'sum' or operation == 'Sum' or operation == '+':

        final_image = image + value

        cv2.imshow('image', image)
        cv2.imshow('after done arithmetic operation', final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif operation == 'minus' or operation == 'Minus' or operation == '-':

        final_image = image - value

        cv2.imshow('image', image)
        cv2.imshow('after done arithmetic operation', final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif operation == 'Multiply' or operation == 'multiply' or operation == '*':

        final_image = image * value

        cv2.imshow('image', image)
        cv2.imshow('after done arithmetic operation', final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif operation == 'Dividing' or operation == 'dividing' or operation == '/':

        final_image = image // value

        cv2.imshow('image', image)
        cv2.imshow('after done arithmetic operation', final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("invalid operation")
        return


if __name__ == "__main__":
    fir_img = str(sys.argv[1])
    const_value = int(sys.argv[2])

    op = str(sys.argv[3])

    arithmetic_operations(fir_img, const_value, op)
