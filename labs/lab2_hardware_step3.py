from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()

while True:
    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, randint(0,255), randint(0,255), randint(0,255))

    time.sleep(0.05)