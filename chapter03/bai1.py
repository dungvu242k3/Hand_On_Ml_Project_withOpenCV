import cv2
import numpy as np

image1 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-dog.jpg")
image2 = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter03/image-cat.jpg")

G = image1.copy()
gp_cat = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gp_cat.append(G)

G = image2.copy()
gp_dog = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gp_dog.append(G)

lp_cat = [gp_cat[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gp_cat[i])
    L = cv2.subtract(gp_cat[i-1], cv2.resize(GE, gp_cat[i-1].shape[1::-1]))
    lp_cat.append(L)

lp_dog = [gp_dog[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gp_dog[i])
    L = cv2.subtract(gp_dog[i-1], cv2.resize(GE, gp_dog[i-1].shape[1::-1]))
    lp_dog.append(L)

LS = []
for l_cat, l_dog in zip(lp_cat, lp_dog):
    rows, cols, dpt = l_cat.shape
    ls = np.hstack((l_cat[:, :cols//2], l_dog[:, cols//2:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

cv2.imshow("KQ",ls_)
cv2.waitKey()
cv2.destroyAllWindows()
