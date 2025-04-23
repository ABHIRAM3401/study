# https://chatgpt.com/c/68079c7e-78c0-8003-afdf-9eab3142d3fc
import cv2
img = cv2.imread(r"c:\Users\abhir\Downloads\e6dacfc4-3343-4cf8-82f5-8cf2e409e601_2.jpeg")
cv2.imshow('image',img)
cv2.waitKey(5000)
print(type(img))
print(img.shape)
print(img[0].shape)

# vid_path = r"C:\Users\abhir\Videos\2024-08-08 21-39-07.mkv"
# video = cv2.VideoCapture(vid_path)
# ret = True
# while ret:
#     ret , frame = video.read()
#     if ret:
#         cv2.imshow('vidoe',frame)
#         cv2.waitKey(40)
# video.release()
cv2.destroyAllWindows()