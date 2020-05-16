from gpiozero import LED
from time import sleep

led = LED(17)

timer = 0.002
while True:
    led.on()
    sleep(timer)
    led.off()
    sleep(3 * timer)
