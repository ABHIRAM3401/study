import cv2

# img = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\panda.jpg")
img = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\sunil-chhetri-kicking-the-ball.jpg")
img = cv2.resize(img , (600,400))
# cv2.imshow("img",img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
# thresh_blur = cv2.blur(thresh,(10,10))
thresh_blur = cv2.medianBlur(thresh,11)
ret , thresh_new = cv2.threshold(thresh_blur,80,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
cv2.imshow("thresh_blur",thresh_blur)
cv2.imshow("thresh_new",thresh_new)




# _, binary     = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
# _, binary_inv = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY_INV)
# _, trunc      = cv2.threshold(img, 80, 255, cv2.THRESH_TRUNC)
# _, tozero     = cv2.threshold(img, 80, 255, cv2.THRESH_TOZERO)
# _, tozero_inv = cv2.threshold(img, 80, 255, cv2.THRESH_TOZERO_INV)

# cv2.imshow("Binary", binary)
# cv2.imshow("Binary Inv", binary_inv)
# cv2.imshow("Trunc", trunc)
# cv2.imshow("ToZero", tozero)
# cv2.imshow("ToZero Inv", tozero_inv)







cv2.waitKey(0)
cv2.destroyAllWindows()