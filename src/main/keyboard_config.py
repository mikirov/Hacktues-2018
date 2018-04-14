import evdev
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
keyboard = list(filter(lambda x: "Keyboard" in x.name or "keyboard" in x.name, devices))[0]
capabilities = keyboard.capabilities(verbose=True)
#print(capabilities)
keyCodes = capabilities[('EV_KEY', 1)]
getkey = lambda key: list(filter(lambda x: key == x[0], keyCodes))[0][1]
#print(keyCodes)

#print(getkey('KEY_W'))
C1_BUTTON_UP = getkey('KEY_W') #W
C1_BUTTON_RIGHT = getkey('KEY_D') #D
C1_BUTTON_DOWN = getkey('KEY_S') #S
C1_BUTTON_LEFT = getkey('KEY_A') #A

C1_LEFT1 = getkey('KEY_LEFTSHIFT') # LSHIFT
C1_LEFT2 = getkey('KEY_SPACE') #SPACE
C1_RIGHT1 = getkey('KEY_F') #F
C1_RIGHT2 = getkey('KEY_G') #G

C2_BUTTON_UP = getkey('KEY_I') #I
C2_BUTTON_LEFT = getkey('KEY_J') #J
C2_BUTTON_DOWN = getkey('KEY_K') #K
C2_BUTTON_RIGHT = getkey('KEY_L') #L

C2_LEFT1 = getkey('KEY_Y') #y
C2_LEFT2 = getkey('KEY_U') #u
C2_RIGHT1 = getkey('KEY_O') #o
C2_RIGHT2 = getkey('KEY_P') #p

EXIT_BUTTON = getkey('KEY_ESC') #ESC
VALID_CODES = [C1_BUTTON_DOWN,C1_BUTTON_LEFT,C1_BUTTON_RIGHT,C1_BUTTON_UP,C1_LEFT1,C1_LEFT2,C1_RIGHT1,C1_RIGHT2,
               C2_BUTTON_DOWN,C2_BUTTON_LEFT,C2_BUTTON_RIGHT,C2_BUTTON_UP,C2_LEFT1,C2_LEFT2,C2_RIGHT1,C2_RIGHT2]

