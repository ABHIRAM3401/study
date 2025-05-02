import cv2
import os
# #IMAGE RESIZE AND CROPPING
# img_path = os.path.join('./images','dogs.jpeg')
# img = cv2.imread(img_path)
# img_resize = cv2.resize(img,(800,600))
# img_crop = img_resize[100:400,250:550]
# cv2.namedWindow('dogs image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('dogs image',1200,600)
# cv2.imshow('dogs image',img)
# # cv2.waitKey(0)
# cv2.imshow('dog resize image',img_resize)
# # cv2.waitKey(0)
# cv2.imshow('dog crop image',img_crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#COLOUR SPACES
img_path = os.path.join('./images','nature.jpg')
img = cv2.imread(img_path)
img_resize = cv2.resize(img,(1250,700))
img_rgb = cv2.cvtColor(img_resize,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
print("pixel values in BGR",img_resize[0,0]," , pixel values in RGB ",img_rgb[0,0])
# cv2.imshow("nature_resize",img_resize)
cv2.imshow("nature_rgb",img_rgb)
# cv2.imshow("nature_hsv",img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()