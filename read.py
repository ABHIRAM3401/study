# https://chatgpt.com/c/68079c7e-78c0-8003-afdf-9eab3142d3fc
import cv2
img = cv2.imread(r"c:\Users\abhir\Downloads\e6dacfc4-3343-4cf8-82f5-8cf2e409e601_2.jpeg")
# img = cv2.imread(r"C:\Users\abhir\Downloads\brownie cake.jpeg")
# print(img.shape)
# resized = cv2.resize(img, (800, 800)) #(widht, height)
# cv2.imshow('image',resized)
# cv2.waitKey(5000)
# print(type(img))
# print(img.shape)
# print(img[0].shape)
#CREATING DIFFRENT NAMED WINDOWS
cv2.imshow('actual',img)
cv2.waitKey(3000)
cv2.destroyAllWindows()  # if i use this line then the acutal image image will be destroyed and the later iamges are visible on the screen , if not one problem will arise , check by commenting this line 

cv2.namedWindow('Normal window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Normal window', 800, 300)

cv2.namedWindow('Keepratio',cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow('Keepratio',400,550)

cv2.imshow('Normal window', img)
cv2.waitKey(3000)
cv2.imshow('keepratio', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


# vid_path = r"C:\Users\abhir\Videos\2024-08-08 21-39-07.mkv"
# video = cv2.VideoCapture(vid_path)
# ret = True
# while ret:
#     ret , frame = video.read()
#     if ret:
#         cv2.imshow('vidoe',frame)
#         cv2.waitKey(40)
# video.release()
# cv2.destroyAllWindows()
