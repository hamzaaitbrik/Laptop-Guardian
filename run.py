from modules import *



if(config['OS'] == 'W'):
    mkdir(f'{getcwd()}\\frames')
elif(config['OS'] == 'L'):
    mkdir(f'{getcwd()}/frames')

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
    imwrite(f'frames\\frame#{i}.jpg', frame)
    log(f'[Main] frame{i} was saved under frames directory.')

i = 1
while(True):
    smile(i)
    i = i +1
    #sleep(0.5)