from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()

while True:
    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(7, 7, 255, 255, 255)
    sense.set_pixel(0, 0, 255, 255, 255)
    sense.set_pixel(7, 0, 255, 255, 255)
    sense.set_pixel(0, 7, 255, 255, 255)
    time.sleep(0.05)
