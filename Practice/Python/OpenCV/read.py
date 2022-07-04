import cv2 as cv

# Reading an image
# img = cv.imread('D:\GIT\Programming\Practice\Python\OpenCV\photos\download.jpg')

# cv.imshow('image', img)

# Reading a video

capture = cv.VideoCapture(r'D:\GIT\Programming\Practice\Python\OpenCV\videos\video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(100) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()