import cv2
img = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\sunil-chhetri-kicking-the-ball.jpg")
edge = cv2.Canny(cv2.resize(img,(1000,600)),200,300)
cv2.imshow('edge',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()