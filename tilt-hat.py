from sense_hat import SenseHat
import time
import os
import sys
from datetime import datetime

sense = SenseHat()
sense.rotation = 270


count = 0

while True:
	orientation = sense.get_orientation_degrees()
	pitch = orientation['pitch']
	pitch = 360 - int(pitch)
	print pitch
	print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
	pitchnow = str(pitch)
	count = count + 1
	if count ==100:
		count = 0
		sense.show_message(pitchnow, text_colour=(255,0,0))
	

