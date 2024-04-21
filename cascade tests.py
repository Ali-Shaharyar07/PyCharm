import cv2
import serial

arduinoData = serial.Serial('COM5', 9600)
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("E:\Code\PyCharm\pythonProject\Cascades\cascades\haarcascade_frontalface_default.xml")

while cap.isOpened():

    ret, image = cap.read()

    image = cv2.resize(image, (900, 600))

    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Cascades Gray", imgGray)

    faces = faceCascade.detectMultiScale(imgGray, 1.7, 5)

    for face in faces:
        x, y, w, h = face
        # print("x=", x, "y=", y, "w=", w, "h=", h)
        mX, mY = x + w, y + h
        cv2.rectangle(image, (x, y), (mX, mY), (255, 150, 40), 2)

    cv2.imshow("Cascades", image)

    if cv2.waitKey(5) & 0xFF == 32:
        break
cap.release()
