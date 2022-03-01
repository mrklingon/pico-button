pins.P3.setPull(PinPullMode.PullUp)
forever(function () {
    if (pins.P3.digitalRead() == false) {
        pins.LED.digitalWrite(true)
    } else {
        pins.LED.digitalWrite(false)
    }
})
