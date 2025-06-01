import cv2

# img = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\panda.jpg")
img = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\sunil-chhetri-kicking-the-ball.jpg")
# cv2.imshow("img",img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
thresh_blur = cv2.blur(thresh,(3,3))
ret , thresh = cv2.threshold(thresh_blur,80,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()