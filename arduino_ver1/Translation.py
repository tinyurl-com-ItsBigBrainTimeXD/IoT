import RPi.GPIO as GPIO
from time import sleep

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Load default font.
font = ImageFont.load_default()

ALARM_MSG = "Alarm Activated"
BUZZER_MSG = "Buzzer Sounding"

def writeWarning(line:tuple):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    for index, value in enumerate(lines):
        draw.text((x, top + 8*index), value,  font=font, fill=255)
    disp.image(image)
    disp.display()
    sleep(5)
    disp.clear()
    disp.display()

#Set warnings off (optional)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) #following printed numbering

# ldr = LightSensor(4)

# ultrasonic = 13
buzzer = 17
servo = 19
# pb = 22
lock = 20

light = 4

def rc_time (light):
    count = 0                                       #Output on the pin for 
    GPIO.setup(light, GPIO.OUT)
    GPIO.output(light, GPIO.LOW)
    sleep(0.1)                                 #Change the pin back to input
    GPIO.setup(light, GPIO.IN)             #Count until the pin goes high
    while (GPIO.input(light) == GPIO.LOW):
        count += 1
    return count 

# GPIO.setup(ultrasonic, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(lock, GPIO.OUT)
GPIO.setup(light, GPIO.IN)
# GPIO.setup(pb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm=GPIO.PWM(servo, 50)
pwm.start(0)

lock_pwm=GPIO.PWM(lock, 50)
lock_pwm.start(0)

position = 0
val = 0

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)
	
def SetLock(angle):
	duty = angle / 18 + 2
	GPIO.output(lock, True)
	lock_pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(lock, False)
	lock_pwm.ChangeDutyCycle(0)


def loop():

	
    while rc_time(light):
    	buzzer_on()
    	print (rc_time(light))
	
    SetLock(0) #unlock
    SetAngle(0) #open

    sleep(5)
    writeWarning()
	
    SetAngle(90)
    sleep(1)
    SetLock(90)
    sleep(5)
    
	


    
#     SetAngle(90) #close
# 	# button will now be a software trigger
#     buzzer_on()
#     buzzer_on()
#     SetAngle(0) #open

#     buzzer_on()
#     buzzer_on()
    
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


# def button_read():
#     while GPIO.input(pb) == GPIO.LOW:
#         print("waiting for pb")
#     print("pb pressed")


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

