import evdev


def find_device(name, case_sensitive=False):
    devices = [evdev.InputDevice(dev) for dev in evdev.list_devices()]
    for dev in devices:
        if name in dev.name or (not case_sensitive and name.lower() in dev.name.lower()):
            return dev

