import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 17

GPIO.setup(led, GPIO.OUT)

timer = 0.003
try: 
    while True:
        GPIO.output(led, 1)
        sleep(timer)
        GPIO.output(led, 0)
        sleep(timer * 3)
finally:
    GPIO.cleanup()
