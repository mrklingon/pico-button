def on_forever():
    pins.LED.digital_write(True)
    pause(200)
    pins.LED.digital_write(False)
    pause(500)
    for index in range(4):
        pins.LED.digital_write(True)
        pause(200)
        pins.LED.digital_write(False)
        pause(500)
forever(on_forever)
