from sense_hat import SenseHat
import time
import os
import sys
from datetime import datetime

sense = SenseHat()
sense.rotation = 180


current  = 0

while True:
	temp = sense.get_temperature()
	temp = temp*9/5 + 32	
	temp = int(temp)
	temp2 = sense.get_temperature_from_pressure()
	temp2 = temp2*9/5 + 32
	temp2 = int(temp2)
	rh = sense.get_humidity()
	rh = int(rh)
	rh = str(rh)
	d = datetime.now()
	Year = "%04d" % (d.year)
	Month = "%02d" % (d.month)
	Date = "%02d" % (d.day)
	Hour = "%02d" % (d.hour)
	Minute = "%02d" % (d.minute)
	Sec = "%02d" % (d.second)
	print Hour, ":", Minute, ":",  Sec, temp, temp2, rh
	rhnow = str(rh)
	sense.show_message(rhnow, text_colour=(255,0,0))
	

