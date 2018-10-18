import pyhook_py3k


def on_keyboard_event(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Ascii:',  event.Ascii,  chr(event.Ascii))
    print('Key:',  event.Key)
    print('KeyID:',  event.KeyID)
    print('ScanCode:',  event.ScanCode)
    print('Extended:',  event.Extended)
    print('Injected:',  event.Injected)
    print('Alt',  event.Alt)
    print('Transition',  event.Transition)
    print('---')
    return True
    #  return True to pass the event to other handlers
    # return False to stop the event from propagating


# create the hook manager
hm = pyhook_py3k
# register two callbacks
hm.KeyDown = on_keyboard_event

# hook into the mouse and keyboard events

if __name__ == '__main__':
    import pythoncom
    pythoncom.PumpMessages()
