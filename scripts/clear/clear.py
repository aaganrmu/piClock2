import time
import Adafruit_SSD1306
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize disp library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
rectangle = (0, 0, width, height)
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle(rectangle, outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
left = 0
right = width

def draw_screen():
    draw.rectangle(rectangle, outline=0, fill=0)
    disp.image(image)
    disp.display()


draw_screen()
