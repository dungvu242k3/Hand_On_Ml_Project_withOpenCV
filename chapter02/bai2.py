import cv2
import numpy as np

img1 = np.ones((512,512,3),np.uint8)*0
cv2.circle(img1,(256,256),200,(255,255,255),-1)
img2 = np.ones((512,512,3),np.uint8)*0
pts1 = np.array([[256,10],[327,171],[195,171]],np.int32)
cv2.fillPoly(img2,[pts1],(255,255,255))

pts2 = np.array([[500,171],[327,171],[371,281]],np.int32)
cv2.fillPoly(img2,[pts2],(255,255,255))

pts3 = np.array([[427,437],[371,281],[256,374]],np.int32)
cv2.fillPoly(img2,[pts3],(255,255,255))

pts4 = np.array([[100,445],[141,281],[256,374]],np.int32)
cv2.fillPoly(img2,[pts4],(255,255,255))

pts5 = np.array([[12,171],[195,171],[141,281]],np.int32)
cv2.fillPoly(img2,[pts5],(255,255,255))

bitwise_xor = cv2.bitwise_xor(img1,img2)
bitwise_xor = cv2.cvtColor(bitwise_xor,cv2.COLOR_BGR2GRAY)
rows, cols = bitwise_xor.shape
noise_white = np.random.choice([0, 1, 255], size=(rows-50, cols-50), p=[0.98, 0.01,0.01])
image1 = cv2.add(bitwise_xor, noise_white.astype(np.uint8))
image2 = cv2.medianBlur(image1,9)
cv2.imshow("anh",image1)
cv2.imshow("kq",image2)
cv2.waitKey()
cv2.destroyAllWindows()