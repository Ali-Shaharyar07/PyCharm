import cv2
import face_recognition as FR
import serial
font = cv2.FONT_HERSHEY_SIMPLEX

arduinoData = serial.Serial('COM5', 9600)

ali = FR.load_image_file("E:\\Code\\PyCharm\\pythonProject\\faces\\ali.jpeg")
faceLoc = FR.face_locations(ali)[0]
aliface_encode = FR.face_encodings(ali)[0]

width = height = 0

knownEncodings = [aliface_encode]
names = ["Ali"]

cap = cv2.VideoCapture(0)
while True:
    ignore, unknownface = cap.read()
    faceLocations = FR.face_locations(unknownface)
    unknownEncodings = FR.face_encodings(unknownface,faceLocations)
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left = faceLocation
        cv2.rectangle(unknownface, (left, top), (right, bottom), (255, 0, 0), 3)
        name = "unknown"
        matches = FR.compare_faces(knownEncodings, unknownEncoding)
        #print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            #print(matchIndex)
           # print(name[matchIndex])
            name=names[matchIndex]
        if name != "unknown":
            cmd = str(left) + "," + str(top) + "," + str(width) + "," + str(height) + ",\r"
            print(cmd)
            arduinoData.write(cmd.encode())
        cv2.putText(unknownface,name,(left,top),font,1,(0,255,0),3)

    cv2.imshow("My faces",unknownface)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cap.release()