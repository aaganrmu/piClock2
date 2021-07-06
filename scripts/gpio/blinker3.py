import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

led_pin = 12
button_pin = 16

class gpio_in:
    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def state(self):
        return GPIO.input(self._pin)

 
class gpio_out:
    def __init__(self, pin):
        self._pin = pin
        self._state = False
        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        if self._state:
            GPIO.output(self._pin, GPIO.HIGH)
        else:
            GPIO.output(self._pin, GPIO.LOW)



led = gpio_out(led_pin)
button = gpio_in(button_pin)

timer = 0.003
try:
    while True:
        
        if button.state():
            led.state = True
            print('pushed')
        else:
            led.state = False
            print('not')
finally:
    GPIO.cleanup()



