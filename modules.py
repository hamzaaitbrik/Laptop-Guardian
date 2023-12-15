from cv2 import VideoCapture, imwrite
from asyncio import get_event_loop
from telegram import Bot
from time import sleep
from datetime import datetime
from os import mkdir, getcwd
from config import config

def log(data):
        print(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - {data}')
        with open('log.txt', 'a') as log:
            log.write(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - {data}\n')