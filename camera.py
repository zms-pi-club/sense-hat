#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep


while True:
   os.system("raspivid -t 100000 -w 1280 -h 1024")
   sleep(1)
       
       
