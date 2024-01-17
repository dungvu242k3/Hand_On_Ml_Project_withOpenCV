import cv2
import numpy as np
img = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

prewitt_kernel_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])
prewitt_kernel_y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

kernelx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
kernely = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
kernel = np.ones((3, 3), np.float32) / 16
sobel = cv2.filter2D(img,-1,laplacian_kernel)

sobelx = cv2.filter2D(sobel,-1,prewitt_kernel_x)

sobely = cv2.filter2D(sobel,-1,prewitt_kernel_y)


sobel_combined1 = cv2.bitwise_xor(sobel,sobelx)
sobel_combined2 = cv2.bitwise_or(sobel,sobely)


cv2.imshow("kq1",sobel_combined1)
cv2.imshow("kq2",sobel_combined2)
cv2.waitKey()
cv2.destroyAllWindows()