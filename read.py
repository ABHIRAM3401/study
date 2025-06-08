# https://chatgpt.com/c/68079c7e-78c0-8003-afdf-9eab3142d3fc 
#https://www.youtube.com/watch?v=eDIj5LuIL4A&t=1695s
import cv2
# img = cv2.imread(r"c:\Users\abhir\Downloads\e6dacfc4-3343-4cf8-82f5-8cf2e409e601_2.jpeg")
# # img = cv2.imread(r"C:\Users\abhir\Downloads\brownie cake.jpeg")
# print(img.shape)
# resized = cv2.resize(img, (800, 800)) #(widht, height)
# # cv2.imshow('image',resized)
# # b = cv2.waitKey(5000)
# # print(b)


# #  line 13 - 23 are added from chatgpt , link is in diary , day 3 27/4
# cv2.imshow('image', resized)
# key = cv2.waitKey(5000) & 0xFF

# if key == ord('q'):
#     print("You pressed q!")
# elif key == ord('s'):
#     print("You pressed s!")
# else:
#     print(f"You pressed key code: {key} , the actual key is {chr(key)}")  #chr() return the alphabet if we give the ascii value as input for that function .

# cv2.destroyAllWindows()

# print(type(img))
# print(img.shape)
# print(img[0].shape)
#CREATING DIFFRENT NAMED WINDOWS
# cv2.imshow('actual',img)
# cv2.waitKey(3000)
# cv2.destroyAllWindows()  # if i use this line then the acutal image image will be destroyed and the later iamges are visible on the screen , if not one problem will arise , check by commenting this line 

# cv2.namedWindow('Normal window', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Normal window', 800, 300)

# cv2.namedWindow('Keepratio',cv2.WINDOW_KEEPRATIO)
# cv2.resizeWindow('Keepratio',400,550)

# cv2.imshow('Normal window', img)
# cv2.waitKey(3000)
# cv2.imshow('keepratio', img)
# cv2.waitKey(3000)
# cv2.destroyAllWindows()


# vid_path = r"C:\Users\abhir\Pictures\Camera Roll\WIN_20250424_21_33_39_Pro.mp4"
# # video = cv2.VideoCapture(vid_path)
# print(type(video))
# ret = True
# cv2.namedWindow('video window',cv2.WINDOW_FULLSCREEN)
# # cv2.resizeWindow('video window',800,500)
# while ret:
#     ret , frame = video.read()
#     if ret:
#         cv2.imshow('video window',frame)
#         cv2.waitKey(40)
# video.release()
# cv2.destroyAllWindows()

#THIS IS FOR WEBCAM
video = cv2.VideoCapture(1)
if not video.isOpened():
    print("Error: Could not open video source.")
    exit()
# ret = True #HERE WE DONT NEED A ret VARIABLE BECAUSE, THERE WILL BE NO END FOR THE FRAMES OF LIVE WEBCAM
cv2.namedWindow('video window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video window',800,500)
while True:
    ret , frame = video.read()
    cv2.imshow('video window',frame)
    if cv2.waitKey(40) & 0xFF == ord('Q'):
        break
video.release()
cv2.destroyAllWindows()

print(cv2.getBuildInformation())


# ?agasabhiram