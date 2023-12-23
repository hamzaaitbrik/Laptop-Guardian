import cv2
import face_recognition
import numpy as np
from dotenv import load_dotenv
import os
from telegram import Bot
from asyncio import get_event_loop
import datetime

isWindows = os.name == 'nt'
isUbuntu = os.name == 'posix'

def whoIsThere(API,chatID, frame, path):
    image_path = f'{path}\\{datetime.datetime.now().strftime(r"%H%M%S")}.jpg' if isWindows else f'{path}/{datetime.datetime.now().strftime(r"%H%M%S")}.jpg'
    cv2.imwrite(image_path, frame)
    async def sendFrame():
        await Bot(token=API).send_photo(chat_id=chatID, photo=open(image_path, 'rb'))
    get_event_loop().run_until_complete(sendFrame())


def initialize_webcam():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open webcam")
    return video_capture

def load_known_faces():
    owner_image = face_recognition.load_image_file("laptop_owner.jpg")
    owner_face_encoding = face_recognition.face_encodings(owner_image)[0]
    known_face_encodings = [owner_face_encoding]
    known_face_names = ["Laptop Owner"]
    return known_face_encodings, known_face_names

def process_frame(frame, known_face_encodings, known_face_names):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    return face_names

