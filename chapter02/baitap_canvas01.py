import cv2
import numpy as np
img = np.ones((512,512,3),dtype = np.uint8) * 255
colors = [(0, 0, 0),   
    (0, 0, 255),     
    (0, 255, 0),     
    (0, 0, 100),     
    (173, 150, 200),  
    (255, 182, 193), 
    (255, 255, 0),   
    (255, 0, 255)]
for i,color in enumerate(colors):
    img[i*64:(i+1)*64,412:512] = color
"""drawing = False
mode = True
ix,iy = -1,-1
def click_draw(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True 
        ix,iy = x,y
        selection_color = img[y,x]
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True :
            if mode == True :
                cv2.rectangle(img,(ix,iy),(x,y),selection_color,1)
            else :
                cv2.circle(img,(x,y),10,selection_color,1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),selection_color,1)
        else :
            cv2.circle(img,(x,y),10,selection_color,1)"""  
def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        selec_color = img[y,x].tolist()
        cv2.circle(img,(x-300,y),30,selec_color,2)
        cv2.rectangle(img,(x-400,y-100),(y-100,x-400),selec_color,2)
cv2.namedWindow("image")
"""cv2.setMouseAllWindow('image',click_draw)
while True:
    cv2.imshow("image",img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q') :
        break"""
cv2.setMouseCallback('image',click)
cv2.imshow("image",img)
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows() 
