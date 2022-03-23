import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12 ,16, 20, 21]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(24, 1)

for j in range(3):
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
        time.sleep(0.2)

GPIO.cleanup()