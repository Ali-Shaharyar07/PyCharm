import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
capture = cv2.VideoCapture(0)


with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while capture.isOpened():

        ret, frame = capture.read()
        frame = cv2.resize(frame, (900, 600))
        frame = cv2.flip(frame, 1)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # Right Hand
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(230, 222, 14), thickness=2, circle_radius=2))

        # Left Hand
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(230, 222, 14), thickness=2, circle_radius=2))


        cv2.imshow('Model Detection', img)

        if cv2.waitKey(10) & 0xFF == ord('\x1b'):
            break


capture.release()
cv2.destroyAllWindows()
