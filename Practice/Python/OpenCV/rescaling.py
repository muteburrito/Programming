from turtle import width
import cv2 as cv

# Reading an image

img = cv.imread('D:\GIT\Programming\Practice\Python\OpenCV\photos\download.jpg')

cv.imshow('image', img)

def rescaleframe(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    # resize image
    resized = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
    return resized

resized_img = rescaleframe(img, 0.5)
cv.imshow('resized_image', resized_img)

capture = cv.VideoCapture(r'D:\GIT\Programming\Practice\Python\OpenCV\videos\video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    cv.imshow('video_rescaled', rescaleframe(frame))
    if cv.waitKey(7) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
