import RPi.GPIO as GPIO
from time import sleep

#Set warnings off (optional)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) #following printed numbering


# ultrasonic = 13
buzzer = 17
servo = 19
pb = 22

# GPIO.setup(ultrasonic, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(pb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm=GPIO.PWM(servo, 50)
pwm.start(0)

position = 0
val = 0

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)


def loop():
    
    SetAngle(90) #close
	# button will now be a software trigger
    buzzer_on()
    buzzer_on()
    SetAngle(0) #open

    buzzer_on()
    buzzer_on()
    
# def button_callback(channel):
#     print("Button was pushed!")
    
    
#     print("ultra is on, press to stop")
#     while button_read():
#         new_ultra()
# #         seeed_ultrasonic()
        
#     print("buzzer is on, press to stop")
#     while button_read():
#         buzzer_sound()
    
#     lid_close()
#     print("Lid closed, waiting for PB")
#     button_read()
#     lid_open()
#     print("Lid open, waiting for PB")
#     button_read()
#     seeed_ultrasonic()


# def button_read_old():
#     while not pb.is_active():
#         time.sleep(0.1)


def button_read():
    while GPIO.input(pb) == GPIO.LOW:
        print("waiting for pb")
    print("pb pressed")


# def lid_close():
#     for i in range(90):
#         servo.value = i / 90 - 1
#         time.sleep(0.15)


# def lid_open():
#     for i in range(90, 0, -1):
#         servo.value = - i / 90

def buzzer_on():
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(0.5)

# def buzzer_sound():
#     buzzer.on()
#     time.sleep(1)
#     buzzer.off()
#     time.sleep(1)


# def seeed_ultrasonic():
#     range_cm = ultrasonic.distance
#     print(range_cm)
#     time.sleep(0.15)

# def new_ultra():
#     try:
#         print(ultrasonicRead(ultrasonic))
#     except TypeError:
#         print "Error"
#     except IOError:
#         print "Error"


if __name__ == '__main__':
    while True:
        loop()

