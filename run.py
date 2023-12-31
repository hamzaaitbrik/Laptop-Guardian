from modules import *



try:
    (lambda: mkdir(f'{getcwd()}\\frames{datetime.now().strftime(r"%d%m%Y")}') if config['OS'] == 'W' else mkdir(f'{getcwd()}/frames{datetime.now().strftime(r"%d%m%Y")}'))()
except:
    pass


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
    imwrite(f'frames{datetime.now().strftime(r"%d%m%Y")}\\frame#{i}.jpg', frame)
    log(f'[Main] frame#{i} was saved under frames directory.')

def whoIsThere(API,chatID,img):
    async def sendFrame():
        await Bot(token=API).send_photo(chat_id=chatID, photo=open(img, 'rb'))
    get_event_loop().run_until_complete(sendFrame())



i = 1
if(config['OS'] == 'W'):
    while(True):
        smile(i)
        whoIsThere(config['TelegramAPI'],config['chatID'],f'{getcwd()}\\frames{datetime.now().strftime(r"%d%m%Y")}\\frame#{i}.jpg')
        log(f'[Main] frame#{i} was sent via Telegram.')
        i = i + 1
elif(config['OS'] == 'L'):
    while(True):
        smile(i)
        whoIsThere(config['TelegramAPI'],config['chatID'],f'{getcwd()}/frames{datetime.now().strftime(r"%d%m%Y")}/frame#{i}.jpg')
        log(f'[Main] frame#{i} was sent via Telegram.')
        i = i +1