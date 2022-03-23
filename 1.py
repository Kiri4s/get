import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12 ,16, 20, 21]

GPIO.setup(leds, GPIO.OUT)

for i in range(8):
        GPIO.output(leds[i], 0)

GPIO.cleanup()