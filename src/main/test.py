import evdev
import select
keyboard = evdev.InputDevice("/dev/input/event0")
fd = keyboard.fd
devs = {fd:keyboard}
while True:
    r,w,x = select.select(devs,[],[])
    print("Device ready.")
    for fd in r:
        for event in keyboard.read():
            print(event)
            #print(event.value == 0)