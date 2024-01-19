import cv2
import numpy as np

img = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernelx = np.array([[-2,0,1],[-1,0,2],[-2,0,1]])
kernely = np.array([[-1,-2,-1],[0,0,0],[1,1,1]])
kernel = np.ones((2, 2) )/ 8
sobel = cv2.filter2D(img,cv2.CV_64F,kernel)

sobelx = cv2.filter2D(img,cv2.CV_64F,kernelx)

sobely = cv2.filter2D(sobel,cv2.CV_64F,kernely)


main_sobel1 = np.sqrt(sobel**2 + sobelx**2)
main_sobel2 = np.sqrt(sobel**2 + sobely**2)

main_sobel1 = cv2.convertScaleAbs(main_sobel1)
main_sobel2 = cv2.convertScaleAbs(main_sobel2)

cv2.imshow("main_sobel",main_sobel1)
cv2.imshow("sobel_combined",main_sobel2)

cv2.waitKey()
cv2.destroyAllWindows()