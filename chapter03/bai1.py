import cv2
import numpy as np

img1 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-cat.jpg")
img2 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-dog.jpg")
G1 = img1.copy()
G2 = img2.copy()
gp1 = [G1]
gp2 = [G2]
for i in range(6):
    G1 = cv2.pyrDown(G1)
    G2 = cv2.pyrDown(G2)
lp1 = [gp1[-1]]
lp2 = [gp2[-1]]
for i in range(5,0,-1):
    lp1.append(cv2.subtract(gp1[i-1], cv2.pyrUp(gp1[i])))
    lp2.append(cv2.subtract(gp2[i-1], cv2.pyrUp(gp2[i])))
LS = []
for  l1,l2 in zip(lp1,lp2):
    rows,cols,dpt = l1.shape
    ls = np.hstack((l1[:,0:cols//2],l2[:,cols//2:]))
    LS.append(ls)
img = LS[0]
for i in range(1,6):
    img = cv2.pyrUp(img)
    img = cv2.add(img,LS[i])
cv2.imshow("KQ",img)
cv2.waitKey()
cv2.destroyAllWindows()