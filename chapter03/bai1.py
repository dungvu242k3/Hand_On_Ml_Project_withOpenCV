import cv2
import numpy as np

img1 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-dog.jpg",1)
img2 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-cat.jpg",1)

height1,width1,_ = img1.shape
height2,width2,_ = img2.shape

blurr1 = cv2.GaussianBlur(img1[:,200:],(15,15),0)
blurr2 = cv2.GaussianBlur(img2[:,:150],(45,45),0)

kq1 = np.copy(img1)
kq2 = np.copy(img2)

kq1[:,200:] = blurr1
kq2[:,:150] = blurr2

kq = cv2.addWeighted(kq1,0.7,kq2,0.2,0)

cv2.imshow("kq",kq)

cv2.waitKey()
cv2.destroyAllWindows()
