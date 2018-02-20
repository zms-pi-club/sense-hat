# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/temperature-2016-10-01-02-44-44.py"

from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
