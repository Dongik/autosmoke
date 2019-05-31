class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def touch_text(self, text):
        self.text = text
        print(text)

def adb_devices():
    return ["device1234"]
