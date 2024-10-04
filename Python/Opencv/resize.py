import cv2 as cv
 
# img = cv.imread('Photo/1.jpg')
# cv.imshow('Image',img)

def rescaleFrame(frame, scale= 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width,height):
    # Live Video
    cap.set(3,width)
    cap.set(4,height)

# Reading videos

cap = cv.VideoCapture(0)

while True:
    isTrue , frame = cap.read()  # read the image by frame variable 
    
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)    
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF== ord('d'): # TO break of the while loop if 'd' is pressed
       break

cap.realease()
cv.destroyAllWindows() 