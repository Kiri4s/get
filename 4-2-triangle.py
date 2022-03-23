import RPi.GPIO as GPIO
import time

def dec2bin(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    T = float(input("Input T: "))
    while True:
        for i in range(0, 256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(T / 256 / 2)
        for i in range(255, 0, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(T / 256 / 2)
except ValueError:
    print("Input Error")
except KeyboardInterrupt:
    print("You've finished the program")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()