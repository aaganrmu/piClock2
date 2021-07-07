import RPi.GPIO as GPIO
from time import sleep

import subprocess

GPIO.setmode(GPIO.BOARD)

led_pin = 12
button_pin = 16
quit_button_pin = 18

class gpio_in:
    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @property
    def state(self):
        return GPIO.input(self._pin) == 0


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
quit_button = gpio_in(quit_button_pin)
shutting_down = False
timer = 0.003
previous_state = False
try:
    while True:
        current_state = button.state
        if current_state != previous_state:
            led.state = current_state
            previous_state = current_state
            if current_state:
                print("now on")
            else:
                print("now off")
        if quit_button.state and not shutting_down:
            shutting_down = True
            subprocess.check_output("sudo shutdown +0", shell=True)

finally:
    GPIO.cleanup()



