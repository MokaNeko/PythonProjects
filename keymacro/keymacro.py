import pyHook
import pythoncom
import win32con
import win32api
import time
KeyUp = win32con.KEYEVENTF_KEYUP


def p(k):
    print("press", k)
    #   win32api.keybd_event(k, 0, 0, 0)
    time.sleep(0.01)


def r(k):
    #   win32api.keybd_event(k, 0, KeyUp, 0)
    print("release", k)
    time.sleep(0.01)


def c(k):
    win32api.keybd_event(k, 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(k, 0, KeyUp, 0)
    time.sleep(0.01)
    #   print("click", k)


def macro(k):
    if k == "K":
        c(86)


class KeyBoardManager:
    keyIsPressed = False

    def on_key_down(self, event):
        if self.keyIsPressed:
            return False
        print(event.Key, 'pressed')
        self.keyIsPressed = True
        return False

    def on_key_up(self, event):
        self.keyIsPressed = False
        print(event.Key, 'released')
        macro(event.Key)
        return False


if __name__ == '__main__':
    my_kb = KeyBoardManager()
    hook_mng = pyHook.HookManager()
    hook_mng.KeyDown = my_kb.on_key_down
    hook_mng.KeyUp = my_kb.on_key_up
    hook_mng.HookKeyboard()
    print('The macro only work for ascii titled windows')
    pythoncom.PumpMessages()
