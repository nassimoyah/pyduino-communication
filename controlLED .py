import cv2
from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("COM4")

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

cap = cv2.VideoCapture(1)
cap.set(3, 1000)  # height
cap.set(4, 600)  # width
while True:

    success, frame = cap.read()

    hands, img = detector.findHands(frame)

    cv2.imshow("nass1", frame)
    if hands:
        hand1 = hands[0]

        fing = detector.fingersUp(hand1)


        if fing == [1,1,1,1,1]:
            arduino.sendData([1])
        elif fing == [0,0,0,0,0]:
            arduino.sendData([0])
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
# capture.release()
cv2.destroyAllWindow
