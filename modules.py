from cv2 import VideoCapture, imwrite
from time import sleep
from datetime import datetime

def log(data):
        print(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - {data}')
        with open('log.txt', 'a') as log:
            log.write(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - {data}\n')