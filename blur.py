import cv2
import os
img_path = os.path.join('./images','freelancer.jpg')
img = cv2.imread(img_path)
img_resized = cv2.resize(img , (800,600))
# cv2.imshow("img_resized",img_resized)

# blur_img7 = cv2.blur(img,(21,21))
blur_img3 = cv2.blur(img,(3,3))
# blur_img70 = cv2.blur(img,(70,70))
blur_img33 = cv2.blur(blur_img3,(3,3))
cv2.imshow("img",img)
cv2.imshow("img blur3",blur_img3)
cv2.imshow("img blur33",blur_img33)
# cv2.imshow("img blur7",blur_img7)
# cv2.imshow("img blur70",blur_img70)

print(img[0,0],blur_img3[0,0],blur_img33[0,0])
cv2.waitKey(0)
cv2.destroyAllWindows()