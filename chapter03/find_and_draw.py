import cv2
import numpy as np

img = cv2.imread("C:/Users/dungv/Projects/Hand_On_Ml_Project_withOpenCV/chapter04/geometric_shapes.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,20,150,apertureSize = 3)
contours,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours :
    perimeter = cv2.arcLength(cnt,True)
    
    approx = cv2.approxPolyDP(cnt,0.011*perimeter,True)
    
    num = len(approx)
    
    if num == 3 :
        cv2.drawContours(img, [approx], 0, (144,96,205), 2)
        cv2.putText(img, "triangle", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (144,96,205), 2)
    elif num == 4:
        cv2.drawContours(img,[approx],0,(0,140,255),2)
        cv2.putText(img, "square", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,140,255), 2)
    elif num == 5:
        cv2.drawContours(img,[approx],0,(105,105,105),2)
        cv2.putText(img, "pentagon", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (105,105,105), 2)
    elif num == 6:
        cv2.drawContours(img,[approx],0,(153,136,119),2)
        cv2.putText(img, "hexagon", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (153,136,119), 2)
        
    elif num == 7:
        cv2.drawContours(img,[approx],0,(255,0,255),2)
        cv2.putText(img, "heptagon", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2)
        
    elif num == 8:
        cv2.drawContours(img,[approx],0,(255,0,0),2)
        cv2.putText(img, "octagon", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
        
    elif num == 9:
        cv2.drawContours(img,[approx],0,(0,100,0),2)
        cv2.putText(img, "nonagon", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,100,0), 2)
        
    else :
        cv2.drawContours(img,[approx],0,(255,255,100),2)
        cv2.putText(img, "circle", tuple(approx[0][0]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,100), 2)
        
        
cv2.imshow("kq",img)
cv2.waitKey()
cv2.destroyAllWindows()
        
        
