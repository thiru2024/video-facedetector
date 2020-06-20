import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\thiru\\Downloads\\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.01,89)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (w+x, y+h), (0, 255, 56), 4)
    cv2.imshow('img', img)
    cv2.waitKey(3000)
    break
cam.release()



