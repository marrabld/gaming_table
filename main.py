import board
import neopixel
import time
import random
from RPi import GPIO
from time import sleep

# For the LEDS
CYCLES = 1000
WAIT = 0.005
NPINS = 45 # + 30 + 15
NDIMS = 20

# For the rotary switch 
clk = 21
dt = 4
push = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(push, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0


pixels = neopixel.NeoPixel(board.D18, NPINS)

# For testing the rotary tool
rotray_cycles = 100000
brightness = 1
clkLastState = GPIO.input(clk)

for j in range(CYCLES):
    pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=brightness)
    pixels.fill((255, 255, 255))

    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if dtState != clkState:
            brightness += 0.1
            print('up')
        
        else:
            brightness -= 0.1
            print('down')
    clkLastState = clkState
    pressState = GPIO.input(push)
    if not pressState:
        print('pressed')
        brightness = 1

    
    pixels.show()
    time.sleep(0.1)


for j in range(CYCLES):
    for i in range(1, NPINS):
        pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=10)
        time.sleep(WAIT)
        random_number_r = random.randint(0, 255)
        random_number_g = random.randint(0, 255)
        random_number_b = random.randint(0, 255)
        pixels.fill((255, 255, 255))
        #pixels[i] = ((random_number_r, random_number_g, random_number_b))
        pixels[i] = ((255, 0, 0))
        #pixels.fill((0,0,0))


for l in range(CYCLES):
    for k in range(CYCLES*NDIMS):
        if CYCLES == 0:
            pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=k/NDIMS)
            pixels.fill((255,0, 0))
            time.sleep(WAIT)
        elif CYCLES == 1:
            pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=k/NDIMS)
            pixels.fill((0, 255, 0))
            time.sleep(WAIT)
        elif CYCLES == 2:
            pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=k/NDIMS)
            pixels.fill((0, 0, 255))
            time.sleep(WAIT)
        
    pixels.fill((0, 0, 0))


for j in range(CYCLES):
    for i in range(1, NPINS):
        time.sleep(WAIT)
        pixels[i] = (255, 0, 125)
        pixels.fill((0, 0, 0))
        #pixels[i-1] = (0, 0, 0)

        
# Randomise the colour
for l in range(CYCLES):
    for k in range(CYCLES*NDIMS):
        pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=k/NDIMS)
        random_number_r = random.randint(0, 255)
        random_number_g = random.randint(0, 255)
        random_number_b = random.randint(0, 255)
        pixels.fill((random_number_r, random_number_g, random_number_b))
        time.sleep(WAIT)
    pixels.fill((0, 0, 0))


pixels.fill((0, 0, 0 ))
time.sleep(WAIT)
pixels.show()


