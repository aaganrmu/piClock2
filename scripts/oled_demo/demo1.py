import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont


WIDTH = 128
HEIGHT = 32

# oled_reset = digitalio.DigitalInOut(board.D4)
# i2c = board.I2C()
# oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D4)
cs_pin = digitalio.DigitalInOut(board.D5)
dc_pin = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc_pin, reset_pin, cs_pin)

image = Image.new("1", (oled.width, oled.height))

draw = ImageDraw.Draw(image)

shape_inner = (0, 0, oled.width, oled.height)
line_width = 3
shape_outer = (line_width, line_width, oled.width - line_width - 1, oled.height - line_width - 1)

draw.rectangle(shape_outer, outline=255, fill=255)
draw.rectangle(shape_inner, outline=0, fill=0)

oled.image(image)
oled.show()
