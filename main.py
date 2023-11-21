import board
import neopixel
import time
import random

CYCLES = 3
WAIT = 0.05
NPINS = 45 + 30 #15
NDIMS = 20

pixels = neopixel.NeoPixel(board.D18, NPINS)

for j in range(CYCLES):
    for i in range(1, NPINS):
        pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=0.05)
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

for j in range(CYCLES):
    time.sleep(0.5)
    pixels.fill((255, 255, 255))
    pixels.show()

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


