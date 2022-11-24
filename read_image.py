import cv2 as cv
import sys

def read_image(path_chart):
    img = cv.imread(path_chart)
    cv.imshow("Display window", img)
    k = cv.waitKey(0)

if __name__ == '__main__':
    read_image('bar-columna1-columna2.png')