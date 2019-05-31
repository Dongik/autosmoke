from autosmoke import Device, adb_devices

device = Device("qwer")

device.touch_text("testsa")

print(adb_devices())
