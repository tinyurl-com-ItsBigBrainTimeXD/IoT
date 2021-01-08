import time
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor, Buzzer, Servo, Device, Button


factory = PiGPIOFactory()
Device.pin_factory = factory
ultrasonic = DistanceSensor(4)
buzzer = Buzzer(7)
servo = Servo(9)
pb = Button(12)
position = 0
val = 0


def loop():
    lid_close()
    print("Lid closed, waiting for PB")
    button_read()
    lid_open()
    print("Lid open, waiting for PB")
    button_read()


def button_read():
    while not pb.is_active():
        time.sleep(0.1)


def lid_close():
    for i in range(90):
        servo.value = i / 90 - 1
        time.sleep(0.15)


def lid_open():
    for i in range(90, 0, -1):
        servo.value = - i / 90


def buzzer_sound():
    buzzer.on()
    time.sleep(1)
    buzzer.off()
    time.sleep(1)


def seeed_ultrasonic():
    range_cm = ultrasonic.distance
    print(range_cm)
    time.sleep(0.15)


if __name__ == '__main__':
    while True:
        loop()

