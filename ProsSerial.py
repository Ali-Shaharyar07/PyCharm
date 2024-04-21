import cv2
import mediapipe as mp
import serial
import math
arduinoData = serial.Serial('COM5', 9600)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands



def _map(x, inMin, inMax, outMin, outMax):
    return int((x-inMin) * (outMax - outMin)/ (inMax - inMin) + outMin)

def constrain(val, min, max):
    if val < min: return min
    if val > max: return max
    return val

def _range(cmd):

    """if cmd >= 0 and cmd < 5: return 0
    if cmd >= 5 and cmd < 10: return 5
    if cmd >= 10 and cmd < 15: return 10
    if cmd >= 15 and cmd < 20: return 15
    if cmd >= 20 and cmd < 25: return 20
    if cmd >= 25 and cmd < 30: return 25
    if cmd >= 30 and cmd < 35: return 30
    if cmd >= 35 and cmd < 45: return 35
    if cmd >= 45 and cmd < 50: return 45
    if cmd >= 50 and cmd < 55: return 50
    if cmd>= 55 and cmd < 60: return 55
    if cmd>= 60 and cmd < 65: return 60
    if cmd >= 65 and cmd < 70: return 65
    if cmd >= 70 and cmd < 75: return 70
    if cmd >= 75 and cmd < 80: return 75
    if cmd >= 80 and cmd < 85: return 80
    if cmd >= 85 and cmd < 90: return 85
    if cmd >= 90 and cmd < 95: return 90

    if cmd >= 95 and cmd < 100: return 95
    if cmd >= 100 and cmd < 105: return 100
    if cmd >= 105 and cmd < 75: return 105
    if cmd >= 110and cmd < 115: return 110
    if cmd >= 120 and cmd < 125: return 115
    if cmd >= 125 and cmd < 130: return 120
    if cmd >= 130 and cmd < 135: return 125
    if cmd >= 135 and cmd < 140: return 130
    if cmd >= 140 and cmd < 145: return 135
    if cmd >= 145 and cmd < 150: return 140
    if cmd >= 150 and cmd < 155: return 145
    if cmd >= 155 and cmd < 160: return 150
    if cmd >= 160 and cmd < 165: return 155
    if cmd >= 165 and cmd < 170: return 165
    if cmd >= 170 and cmd < 175: return 175
    if cmd >= 175 and cmd <= 180: return 180
    """
    if cmd >= 0 and cmd < 10: return 5
    if cmd >= 10 and cmd < 20: return 15
    if cmd >= 20 and cmd < 30: return 25
    if cmd >= 30 and cmd < 40: return 35
    if cmd >= 40 and cmd < 50: return 45
    if cmd >= 50 and cmd < 60: return 55
    if cmd >= 60 and cmd < 70: return 65
    if cmd >= 70 and cmd < 80: return 75
    if cmd >= 80 and cmd < 90: return 85
    if cmd >= 90 and cmd < 100: return 95
    if cmd >= 100 and cmd < 110: return 105
    if cmd >= 110 and cmd < 120: return 115
    if cmd >= 120 and cmd < 130: return 125
    if cmd >= 130 and cmd < 140: return 135
    if cmd >= 140 and cmd < 150: return 145
    if cmd >= 150 and cmd < 160: return 155
    if cmd >= 160 and cmd < 170: return 165
    if cmd >= 170 and cmd <= 180: return 180


Ix = Iy = Wx = Wy = Mx = My = Rx = Ry = Px = Py = Tx = Ty = 0.0
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:

        for ids, landmrk in enumerate(hand_landmarks.landmark):
            if ids == 0 :
                Wx, Wy = landmrk.x * image_width, landmrk.y * image_height
            if ids == 8:
                Ix, Iy = landmrk.x * image_width, landmrk.y * image_height
            if ids == 12:
                Mx, My = landmrk.x * image_width, landmrk.y * image_height
            if ids == 16:
                Rx, Ry = landmrk.x * image_width, landmrk.y * image_height
            if ids == 20:
                Px, Py = landmrk.x * image_width, landmrk.y * image_height
            if ids == 4:
                Tx, Ty = landmrk.x * image_width, landmrk.y * image_height
        if Wx >= Tx:
            distThumb = 0
        else:
            distThumb = abs(Tx)-abs(Wx)
        distPinky = math.sqrt((Px - Wx) ** 2 + (Py - Wy) ** 2)
        distRing = math.sqrt((Rx - Wx) ** 2 + (Ry - Wy) ** 2)
        distMiddle = math.sqrt((Mx - Wx) ** 2 + (My - Wy) ** 2)
        distIndex = math.sqrt((Ix-Wx)**2 + (Iy-Wy)**2)


        cmdIndex = _range(_map(constrain(distIndex, 55, 110), 55, 110, 0, 180))
        cmdMiddle =_range( _map(constrain(distMiddle, 55, 110), 55, 110, 0, 180))
        cmdRing = _range(_map(constrain(distRing, 55, 110), 55, 110, 0, 180))
        cmdPinky = _range(_map(constrain(distPinky, 40, 100), 40, 100, 0, 180))
        cmdThumb = _range(_map(constrain(distThumb, 20, 50), 20, 50, 0, 180))


        cmdIndex = str(cmdIndex) + ","
        cmdMiddle = str(cmdMiddle) + ","
        cmdRing = str(cmdRing) + ","
        cmdPinky = str(cmdPinky) + ",\r"
        cmdThumb = str(cmdThumb) + ","

        cmdH = cmdThumb + cmdIndex + cmdMiddle + cmdRing + cmdPinky
        print(cmdH)
        arduinoData.write(cmdH.encode())





        #print("Index Distance: ", distIndex)     #135  se 30/20
        #print("Middle Distance: ", distMiddle) #130 se 30/20
        #print("Ring Distance: ", distRing) # 130 se 30
        #print("Pinky Distance: ", distPinky) #100 se 30/40
        # print("Thumb Distance (X): ", distThumb) #70s se low 10s

        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()