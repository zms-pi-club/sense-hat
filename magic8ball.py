import random
import time
from sense_hat import SenseHat
sh = SenseHat()
sh.show_message("Ask a Question & shake", scroll_speed = (0.3))
time.sleep(3)
replies = ['signs point to yes','Without a doubt','You may rely on it']


while True:
    x, y, z = sh.get_accelerometer_raw(),values()
    x = abc(x)
    y = abc(y)
    z = abc(z)
    if x > 2 y > 2 z > 2 :
    sh.show_message(random.choice(replies), scroll_speed(0.3))
    else:
        sh.clear()
 
