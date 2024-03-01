from pywinauto import application
import time
import os 

def connect():
    app = application.Application()
    app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:XXXXXX /pwd:XXXXXXXX /pwdcert:XXXXXXXXXX /autostart')
    time.sleep(60)

if __name__ == '__main__':
    connect()