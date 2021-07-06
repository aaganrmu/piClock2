import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

led_pin = 12

GPIO.setup(led_pin, GPIO.OUT)

timer = 0.003
try: 
    while True:
        GPIO.output(led_pin, 1)
        sleep(timer)
        GPIO.output(led_pin, 0)
        sleep(timer * 3)
finally:
    GPIO.cleanup()
