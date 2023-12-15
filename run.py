from modules import *



(lambda: mkdir(f"{getcwd()}\\frames") if config['OS'] == 'W' else mkdir(f"{getcwd()}/frames"))()


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

def whoIsThere(API,chatID,img):
    async def sendFrame(API,chatID):
        await Bot(token=API).send_photo(chat_id=chatID, photo=open(img, 'rb'))
    get_event_loop().run_until_complete(sendFrame(API,chatID))



i = 1
while(True):
    smile(i)
    whoIsThere(config['TelegramAPI'],config['chatID'])
    i = i +1
    #sleep(0.5)