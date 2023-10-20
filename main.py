import cv2
import mediapipe as mp



def coordinate(id, h, w):
    cx, cy = int(lm.x * w), int(lm.y * h)
    cv2.circle(image, (int(cx), int(cy)), 2, (255, 255, 255), cv2.FILLED)
    return cx,cy


mpHands = mp.solutions.hands
hands = mpHands.Hands()


# For webcam input:

url = 'http://192.168.1.7:4747/video'
cap = cv2.VideoCapture(url)


while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      break

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    #processing
    result = hands.process(imgRGB)

    h,w,c = image.shape
    handsUp = 0
    thumbIsCorrect = 0


    #drawing circuls at landmarks

    if result.multi_hand_landmarks:
        for handsLMS in result.multi_hand_landmarks:
            for id, lm in enumerate(handsLMS.landmark):
                cx,cy = coordinate(id,h,w)


    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(1) & 0xFF == 27:
      break

cap.release()
cv2.destroyAllWindows()