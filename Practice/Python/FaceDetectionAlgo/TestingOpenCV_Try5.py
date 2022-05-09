import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 100)


# cv2.imshow('Output', img)
# cv2.waitKey(0)



while True:
    success, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w ,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0),2)
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break