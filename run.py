from modules import *

def take_photo(i):
    webcam = VideoCapture(0)
    if not webcam.isOpened():
        print("Error: Unable to access the webcam")
        return
    ret, frame = webcam.read()
    if not ret:
        print("Error: Unable to capture a frame")
        return
    webcam.release()
    imwrite(f'frame#{i}.jpg', frame)

i = 1
while(True):
    take_photo(i)
    i = i +1
    sleep(0.5)