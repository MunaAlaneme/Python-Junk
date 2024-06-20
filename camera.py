import cv2
import time

camera = cv2.VideoCapture(0) # 0 represents your webcam.

while True:
    _, frame = camera.read()
    pic = ("picture.png", frame)
    cv2.imshow("LIVEFEED", frame)
    time.sleep(10)
    break