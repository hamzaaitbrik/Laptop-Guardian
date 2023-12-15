from modules import log
config = dict()

def getOS():
    OS = input('\n--> ').upper()
    if(OS not in ['L', 'W']):
        log('[SETUP] Insert L for Linux, and W for Windows.')
        return getOS()
    return OS

def setTelegram():
    log('[SETUP] Insert your Telegram API. Make sure it is correct before you proceed.')
    TelegramAPI = input('\n--> ')
    return TelegramAPI

def getInfos():
    log('[SETUP] What operating system are you running? Please, insert L for Linux and W for Windows.')
    config['OS'] = getOS()
    config['TelegramAPI'] = setTelegram()
    print(config)


getInfos()