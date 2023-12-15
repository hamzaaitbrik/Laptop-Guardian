from modules import log



def getInfos():
    def getOS():
        log('[SETUP] What operating system are you running? Please, insert W for Windows and L for Linux.')
        OS = input()
        while(OS not in ['L', 'W']):
            getOS()
        print(OS)
    getOS()



getInfos()