import cv2

image = cv2.imread("demo.jpg")


# Convert from one color space to another
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

# Image Smotthing
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Save our image
cv2.imwrite("grey.png", grey_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
