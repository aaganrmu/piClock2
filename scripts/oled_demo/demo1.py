import board
import busio
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)

WIDTH = 128
HEIGHT = 32

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

