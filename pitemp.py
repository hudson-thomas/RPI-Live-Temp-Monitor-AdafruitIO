# Import modules (read README in github repo for info on prerequisites)
import time
import digitalio
import os
from gpiozero import CPUTemperature

# import REST client
from Adafruit_IO import Client, Feed, RequestError

# You AIO key
ADAFRUIT_IO_KEY = 'YOUR_KEY'

# Your AIO username.
ADAFRUIT_IO_USERNAME = 'YOUR_USERNAME'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'pitemp' feed
    tempfeed = aio.feeds('pitemp')
except RequestError: # create a digital feed
    tempfeed = Feed(name="pitemp")
    tempfeed = aio.create_feed(pitemp)


while True:
    cpu = CPUTemperature()
   # Debug wrong temp by uncommenting line below.
   # print(cpu.temperature)


    print('pitemp -> ',  cpu.temperature)
    aio.send(tempfeed.key, cpu.temperature)

    # Avoid timeout by setting sleep to 3+ seconds. 30 works fine for me
    time.sleep(30)
