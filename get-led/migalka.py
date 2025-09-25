import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds1 = [24, 22, 23, 27]
leds2 = [17, 25, 12, 16]
button = 13
right = 10
left = 9
GPIO.setup(leds1, GPIO.OUT)
GPIO.setup(leds2, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)
GPIO.setup
GPIO.output(leds1, 0)
GPIO.output(leds2, 0)
short_time = 0.07
long_time = 0.2

while True:
    if GPIO.input(button):
        GPIO.output(leds1, 1)
        time.sleep(short_time)
        GPIO.output(leds1, 0)
        GPIO.output(leds2, 1)
        time.sleep(short_time)
        GPIO.output(leds2, 0)
    if not GPIO.input(button) and not GPIO.input(left) and not GPIO.input(right):
        GPIO.output(leds1, 1)
        time.sleep(long_time)
        GPIO.output(leds1, 0)
        time.sleep(short_time)
        GPIO.output(leds2, 1)
        time.sleep(long_time)
        GPIO.output(leds2, 0)
        time.sleep(short_time)