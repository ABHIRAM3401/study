import cv2
import os
img_path = os.path.join('./images','freelancer.jpg')
img = cv2.imread(img_path)
img_resized = cv2.resize(img , (800,600))
# cv2.imshow("img_resized",img_resized)

# blur_img7 = cv2.blur(img,(21,21))
# blur_img3 = cv2.blur(img,(3,3))
# blur_img70 = cv2.blur(img,(70,70))
# blur_img33 = cv2.blur(blur_img3,(3,3))

# cv2.imshow("img",img)
# cv2.imshow("img blur3",blur_img3)
# # cv2.imshow("img blur33",blur_img33)
# cv2.imshow("img blur7",blur_img7)
# cv2.imshow("img blur70",blur_img70)

# print(img[0,0],blur_img3[0,0],blur_img33[0,0])

#GAUSSIAN BLUR
# img_gaussian_blur_deviation5 = cv2.GaussianBlur(img,(7,7),5)
# img_gaussian_blur_deviation11 = cv2.GaussianBlur(img,(7,7),11)
# cv2.imshow("gaussian_blur5" , img_gaussian_blur_deviation5)
# cv2.imshow("gaussian_blur11" , img_gaussian_blur_deviation11)
# print(img_gaussian_blur_deviation5[0,0] , img_gaussian_blur_deviation11[0,0])

#MEDIAN BLUR

# cv2.imshow("img",cv2.medianBlur(img,11))

# noise_img = cv2.imread(os.path.join('./images','pepper_man.jpg'))
# median_blur = cv2.medianBlur(noise_img,7) #upon increasing the kernel size  ,the white dots are vanishing 

# noise_img_cow = cv2.imread(os.path.join('./images','cow-salt-peper.png'))
# # median_blur_cow = cv2.GaussianBlur(noise_img_cow,(3,3),7) #smear effect
# median_blur_cow = cv2.medianBlur(noise_img_cow,7)

# cv2.imshow("median_blur",median_blur)
# cv2.imshow("median_blur_cow",median_blur_cow)

cv2.waitKey(0)
cv2.destroyAllWindows()