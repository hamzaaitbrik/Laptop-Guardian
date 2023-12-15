from modules import *



def smile(i):
    webcam = VideoCapture(0)
    if not webcam.isOpened():
        log('[Main] Unable to access the webcam.')
        return
    isTaken, frame = webcam.read()
    if not isTaken:
        log('[Main] Unable to capture frames.')
        return
    webcam.release()
    imwrite(f'{getcwd()}\\frames\\frame#{i}.jpg', frame)

i = 1
while(True):
    smile(i)
    i = i +1
    #sleep(0.5)