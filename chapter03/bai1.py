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


kq = 1.3*kq1 + 0.15*kq2 + -75
kq = np.clip(kq,10,255).astype('uint8')
kq3 = 0.2*kq1 + 0.7*kq2 + -10
kq3 = np.clip(kq3,0,255).astype('uint8')
result = cv2.addWeighted(kq,0.5,kq3,0.55,-40)
#cv2.imshow("kq",kq)
#cv2.imshow("kq3",kq3)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()
