import cv2 as cv
import numpy as np



def findCircles(imgname):
    img = cv.imread(imgname)
    hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsvImg, (0,50,20), (15,255,255)) + cv.inRange(hsvImg, (170,50,20), (180,255,255))
    masked = cv.bitwise_and(img, img, mask=mask)
    gray = cv.cvtColor(masked, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    result = img.copy()
    if circles is not None:
        circles = np.round(circles).astype(int)
        for i in circles[0, :]:
            center = (i[0], i[1])
            result = cv.circle(result, center, i[2], (0,0,0), 3)
    return result



def getOutput(imgname):
    cv.imwrite('./output/' + imgname + '.jpg', findCircles('./pictures/' + imgname + '.jpg'))

getOutput('red')
getOutput('a')
getOutput('b')
getOutput('c')
getOutput('d')
getOutput('e')
getOutput('f')
getOutput('g')
getOutput('h')