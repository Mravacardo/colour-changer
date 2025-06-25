import cv2

image = cv2.imread('bird2.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
cv2.imshow("original", image)
cv2.imshow("weird colour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
