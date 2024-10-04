import cv2 as cv
# reading images

# img = cv.imread('Photo/cat.jpg')
# cv.imshow("Image",img)

# reading videos
cap = cv.VideoCapture(0)

while True:
    isTrue , frame = cap.read()  # read the image by frame variable 
    cv.imshow('Video', frame)    # To show the video by frame

    if cv.waitKey(20) & 0xFF== ord('d'): # TO break of the while loop if 'd' is pressed
       break

cap.realease()
cv.destroyAllWindows() 