import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)

p.start(0)

try:
    while True:
        try:
            x = int(input("input duty cycle: "))
            if x < 0 or x > 100:
                print("Input Error")
                continue
            p.ChangeDutyCycle(x)
            print(3.3 * x /100, "B")
        except ValueError:
            print("Input Error")
            continue
except KeyboardInterrupt:
    print("You've finished the program")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()