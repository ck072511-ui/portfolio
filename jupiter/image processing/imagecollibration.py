import cv2
import numpy as np
img = cv2.imread("jupiter/image processing/vichle.jpeg")
rows, cols = img.shape[:2]

tx, ty = 50, 30

M = np.float32([[1, 0, tx],[0, 1, ty]])
translated = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Translated image",translated)
# cv2.waitkey(0)
cv2.destroyAllWindows()

# import cv2
# img=cv2.imread("jupiter/image processing/vichle.jpeg")

scaled = cv2.resize(img,None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaled Image",scaled)
# cv2.waitkey(0)
cv2.destroyAllWindows()
