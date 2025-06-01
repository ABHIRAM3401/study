import cv2
img_path = r"C:\Users\abhir\Documents\OpenCV\images\eye.jpeg"
img = cv2.imread(img_path)
# img = cv2.resize(img,(800,600))

img_gray = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
# img_gray = cv2.resize(img_gray,(800,600))

img_reduced = cv2.imread(img_path , cv2.IMREAD_REDUCED_COLOR_2)  #used to reduce the size of the image by half , 1/4 or 1/8 , in the same way we can load the image as grayscale and reduce  the size at a time by     cv2.IMREAD_REDUCED_GRAYSCALE_2

# #img_gdal = cv2.imread(img_path,cv2.IMREAD_LOAD_GDAL)

cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)
cv2.imshow("img_reduced",img_reduced)
# #cv2.imshow("img_gdal",img_gdal)

cv2.waitKey(0)
cv2.destroyAllWindows()