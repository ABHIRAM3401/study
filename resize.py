#i didn't understand how the resize of an image is happening but copying the code from gpt https://chatgpt.com/c/68451456-aa54-8003-b48c-28f0a3321078  https://chatgpt.com/share/684591c7-66a4-8003-a435-0e5058035d4a
import cv2

# Load image
image = cv2.imread(r"C:\Users\abhir\Documents\OpenCV\images\eye.jpeg")  # Replace with your image path

# 1. Resize using explicit size
resized_dsize = cv2.resize(image, (400, 300))  # width=400, height=300

# 2. Resize using scaling factors
resized_scale = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Resized with dsize (400x300)", resized_dsize)
cv2.imshow("Resized with fx=2.0, fy=2.0", resized_scale)

cv2.waitKey(0)
cv2.destroyAllWindows()
