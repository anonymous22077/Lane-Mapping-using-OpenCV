import cv2
import numpy as np


def region_of_interest(image,vertices):
    
    mask = np.zeros_like(image)
    match_mask_color = 255  
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

def nothing(x):
    pass

window_width = 300
window_height = 300

cv2.namedWindow('Threshold Adjustment',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Threshold Adjustment',window_width,window_height)
cv2.createTrackbar('RED','Threshold Adjustment',0,255,nothing)
cv2.createTrackbar('GREEN','Threshold Adjustment',0,255,nothing)
cv2.createTrackbar('BLUE','Threshold Adjustment',0,255,nothing)
cv2.createTrackbar('low threshold','Threshold Adjustment',50,400,nothing)
cv2.createTrackbar('high threshold','Threshold Adjustment',10,308,nothing)
cv2.createTrackbar('threshold','Threshold Adjustment',10, 200, nothing)
cv2.createTrackbar('miniLineLength', 'Threshold Adjustment', 10, 200, nothing)
cv2.createTrackbar('maxLineGap', 'Threshold Adjustment', 50, 400, nothing)
cv2.createTrackbar('Line Thickness','Threshold Adjustment',1,10,nothing)

def draw_the_lines(img, lines):
    B = cv2.getTrackbarPos('BLUE', 'Threshold Adjustment')
    G = cv2.getTrackbarPos('GREEN','Threshold Adjustment')
    R = cv2.getTrackbarPos('RED','Threshold Adjustment')

    copied_image = np.copy(img)
    blank_image = np.zeros((copied_image.shape[0],copied_image.shape[1],3),dtype=np.uint8)

    T=cv2.getTrackbarPos('Line Thickness','Threshold Adjustment')

    if lines is not None: 
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_image,(x1,y1),(x2,y2),(B,G,R),thickness=T) 


    copied_image = cv2.addWeighted(copied_image,0.8,blank_image,1,0)
    return copied_image

def process(image):
    
    roi_points = [(200,image.shape[0]),(550,250),(750,350),(image.shape[1]-200,image.shape[0])]

    lt = cv2.getTrackbarPos('low threshold','Threshold Adjustment')
    ht = cv2.getTrackbarPos('high threshold','Threshold Adjustment')

    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image,(5,5),0)
    cny_img = cv2.Canny(blurred_image,lt,ht)
    cropped = region_of_interest(cny_img,np.array([roi_points],np.int32))

    t = cv2.getTrackbarPos('threshold','Threshold Adjustment')
    mll = cv2.getTrackbarPos('miniLineLength','Threshold Adjustment')
    mlg = cv2.getTrackbarPos('maxLineGap','Threshold Adjustment')

    lines = cv2.HoughLinesP(cropped,rho=1,theta=np.pi / 180,threshold=t,minLineLength=mll,maxLineGap=mlg)
    imgWithLines = draw_the_lines(image,lines)
    return imgWithLines

cap = cv2.VideoCapture('Road view2.mp4')
resizewidth = 800
resizeheight = 570

while cap.isOpened():

    ret,frame = cap.read()
    if not ret:  
        break

    processed_frame = process(frame)
    resized_frame = cv2.resize(processed_frame,(resizewidth,resizeheight))
    cv2.imshow('Lane Mapping Testing',resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
                                        