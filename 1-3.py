import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

while True:
    GPIO.output(5, GPIO.input(6))
    time.sleep(2)
