import board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont


WIDTH = 128
HEIGHT = 32

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))

draw = ImageDraw.Draw(image)

shape_inner = (0, 0, oled.width, oled.height)
line_width = 3
shape_outer = (line_width, line_width, oled.width - line_width - 1, oled.height - line_width - 1)

draw.rectangle(shape_outer, outline=255, fill=255)
draw.rectangle(shape_inner, outline=0, fill=0)

oled.image(image)
oled.show()
