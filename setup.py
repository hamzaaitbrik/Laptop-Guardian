from modules import log
config = dict()

def getOS():
    log('[SETUP] What operating system are you running? Please, insert L for Linux and W for Windows.')
    OS = input().upper()
    if(OS not in ['L', 'W']):
        log('[SETUP] Insert L for Linux, and W for Windows.')
        return getOS()
    return OS



def getInfos():
    config['OS'] = getOS()
    print(config)


getInfos()