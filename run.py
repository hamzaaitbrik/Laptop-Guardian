from datetime import datetime
from os import mkdir, getcwd
from config import config
from modules import log
from face_id import whoIsThere
import os
from dotenv import load_dotenv
from face_id import initialize_webcam, load_known_faces, process_frame

isWindows = os.name == 'nt'
isUbuntu = os.name == 'posix'

path = f'{getcwd()}\\frames{datetime.now().strftime(r"%d%m%Y")}' if isWindows else f'{getcwd()}/frames{datetime.now().strftime(r"%d%m%Y")}'

try:
    mkdir(path)
except FileExistsError:
    pass

def main():
    video_capture = initialize_webcam()
    known_face_encodings, known_face_names = load_known_faces()
    process_this_frame = True

    while True:
        isTaken, frame = video_capture.read()
        if process_this_frame:
            face_names = process_frame(frame, known_face_encodings, known_face_names)

            if len(face_names) == 0:
                print("No one is using the laptop")
            elif "Laptop Owner" in face_names:
                print("Laptop Owner is using the laptop")
            else:
                load_dotenv()
                API = os.getenv("TelegramAPI")
                chatID = os.getenv("chatID")
                whoIsThere(API,chatID, frame, path)

if __name__ == "__main__":
    main()


