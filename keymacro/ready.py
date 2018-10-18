import pyHook
import pythoncom


class KeyBoardManager:
    keyIsPressed = False

    def on_key_down(self, event):
        if self.keyIsPressed:
            return False
        print(str(event.Key) + ' is pressed')
        self.keyIsPressed = True
        return False

    def on_key_up(self, event):
        self.keyIsPressed = False
        print(str(event.Key) + ' is released')
        return False


if __name__ == '__main__':
    my_kb = KeyBoardManager()
    hook_mng = pyHook.HookManager()
    hook_mng.KeyDown = my_kb.on_key_down
    hook_mng.KeyUp = my_kb.on_key_up
    hook_mng.HookKeyboard()
    pythoncom.PumpMessages()
