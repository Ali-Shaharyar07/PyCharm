import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
import math

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

        distThumb = abs(Tx)-abs(Wx)
        distPinky = math.sqrt((Px - Wx) ** 2 + (Py - Wy) ** 2)
        distRing = math.sqrt((Rx - Wx) ** 2 + (Ry - Wy) ** 2)
        distMiddle = math.sqrt((Mx - Wx) ** 2 + (My - Wy) ** 2)
        distIndex = math.sqrt((Ix-Wx)**2 + (Iy-Wy)**2)

        #print("Index Distance: ", distIndex)
        #print("Middle Distance: ", distMiddle)
        #print("Ring Distance: ", distRing)
        #print("Pinky Distance: ", distPinky)
        #print("Thumb Distance (X): ", distThumb)

        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()