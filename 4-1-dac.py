import RPi.GPIO as GPIO

def dec2bin(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        try:
            x = input("Input number from 0 to 255: ")
            if x == 'q':
                print("You've finished the programm")
                break
            if float(x) % 1 != 0:
                print("Error: float input")
                continue
            x = int(x)
            if x > 255 or x < 0:
                print("Error: anable value (0 <= value <= 255)")
                continue 
            GPIO.output(dac, dec2bin(x))
            print(3.3 / 256 * x, "B")
        except ValueError:
            print("Error: string input")
            continue
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()