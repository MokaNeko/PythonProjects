#import msvcrt
import win32con
import win32api
import time

U = win32con.KEYEVENTF_KEYUP


def p(k):
    win32api.keybd_event(k, 0, 0, 0)
    time.sleep(1)


def r(k):
    win32api.keybd_event(k, 0, U, 0)


def get():
    k = 68
        #ord(msvcrt.getch())
    print('org', k)
    return k


'''
win32api.keybd_event(91, 0, 0, 0)  # 键盘按下 91win
time.sleep(1)
win32api.keybd_event(77, 0, 0, 0)  # 键盘按下  68  D
time.sleep(1)
win32api.keybd_event(77, 0, UP, 0)  # 键盘松开  D 68
win32api.keybd_event(91, 0, UP, 0)  # 键盘松开
'''
key = get()
if key == 68:
    print(key)
    p(91)
    p(68)
    r(68)
    r(91)
