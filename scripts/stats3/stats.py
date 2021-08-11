import time
import lib_sh1106
import subprocess
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from smbus import SMBus

i2cbus = SMBus(1)
oled = sh1106(i2cbus)
draw = oled.canvas





# # Create blank image for drawing.
# # Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
print("Height: " + str(height) + " Width: " + str(width))
rectangle = (0, 0, width, height)

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
left = 0
right = width
# Move left to right keeping track of the current x position for drawing shapes.

# Load default font.
font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)


def cmd_result(cmd):
    result_bytes = subprocess.check_output(cmd, shell=True)
    result_string = result_bytes.decode('utf-8')
    return result_string


def draw_text(text, line):
    x = left
    y = top + 8 * line
    draw.text((x, y), text, font=font, fill=255)


def draw_screen():
    draw.rectangle(rectangle, outline=0, fill=0)

    IP = cmd_result("hostname -I | cut -d\' \' -f1")
    CPU = cmd_result("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'")
    MEM = cmd_result("free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'")
    # HDD = cmd_result("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'")
    TIME = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    texts = [IP, CPU, MEM, TIME]

    for line, text in enumerate(texts):
        draw_text(text, line=line)

    oled.display()

def clear_screen():
    draw.rectangle(rectangle, outline=0, fill=0) 
    oled.cls()

try:
    while True:
        draw_screen()
finally:
    clear_screen()