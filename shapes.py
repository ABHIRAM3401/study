import cv2
img = cv2.resize(cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\eye.jpeg"),(800,600))

# cv2.line(img,(100,200),(500,500),(0,0,0),4)
cv2.line(img,(110,85),(650,500),(0,0,0),4)
cv2.rectangle(img,(110,85),(650,500),(255,0,0),4)
# cv2.rectangle(img,(70,120),(600,400),(0,0,0),4)
cv2.circle(img,(378,270),55,(0,255,0),3)
# cv2.circle(img,(380,280),55,(0,0,255),5)
cv2.putText(img,"gurthukuvundha",(378,270),cv2.FONT_HERSHEY_COMPLEX,4,(123,321,213),3)
cv2.imshow('img',img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()