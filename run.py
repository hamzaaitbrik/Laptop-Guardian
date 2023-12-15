import cv2
from time import sleep

def take_photo(i):
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Error: Unable to access the webcam")
        return
    ret, frame = webcam.read()
    if not ret:
        print("Error: Unable to capture a frame")
        return
    webcam.release()
    cv2.imwrite(f'frame#{i}.jpg', frame)

i = 1
while(True):
    take_photo(i)
    i = i +1
    sleep(0.5)