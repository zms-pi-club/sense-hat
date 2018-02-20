from sense_hat import SenseHat
import time
import os
import sys
from datetime import datetime

sense = SenseHat()
sense.rotation = 180


count = 0

while True:
	orientation = sense.get_orientation_degrees()
	roll = orientation['roll']
	roll = int(roll)
	print roll
	print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
	rollnow = str(roll)
	count = count + 1
	if count ==100:
		count = 0
		sense.show_message(rollnow, text_colour=(255,0,0))
	

