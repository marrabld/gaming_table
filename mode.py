import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel

# Rotary Encoder Pins
Enc_A = 21  
Enc_B = 4  

# Push Button Pin
push = 27

# NeoPixel Setup
NPINS = 45 * 2
brightness = 0.5  # Starting brightness
mode = "brightness"  # Modes: "brightness" or "color"
color_index = 0  # Index to keep track of the current color
bright_res = 0.025

# Initialize the NeoPixel
pixels = neopixel.NeoPixel(board.D18, NPINS, brightness=brightness)

# Define a color wheel (Red to Blue, for example)
color_wheel = [
    (255, 0, 0),   # Red
    (255, 127, 0), # Orange
    (255, 255, 0), # Yellow
    (0, 255, 0),   # Green
    (0, 0, 255)    # Blue
]

color_wheel = [
    (255, 0, 0),      # Red
    (255, 64, 0),     # Red-Orange
    (255, 128, 0),    # Orange-Red
    (255, 191, 0),    # Orange
    (255, 255, 0),    # Yellow
    (191, 255, 0),    # Yellow-Green
    (128, 255, 0),    # Green-Yellow
    (64, 255, 0),     # Green
    (0, 255, 64),     # Green-Cyan
    (0, 255, 128),    # Cyan-Green
    (0, 255, 191),    # Cyan
    (0, 255, 255),    # Light Blue
    (0, 191, 255),    # Sky Blue
    (0, 128, 255),    # Azure
    (0, 64, 255),     # Blue
    (64, 0, 255),     # Blue-Violet
    (128, 0, 255),    # Violet
    (191, 0, 255),    # Purple
    (255, 0, 255),    # Magenta
    (255, 0, 191),    # Pink
    (255, 0, 128),    # Rose
    (255, 0, 64),     # Red-Pink
    (0, 0, 0)         # black
]


def init():
    print("Rotary Encoder and Button Test Program")

    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)

    GPIO.setup(push, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(push, GPIO.FALLING, callback=toggle_mode, bouncetime=200)

    pixels.fill(color_wheel[0])  # Start with the first color in the wheel

def toggle_mode(channel):
    global mode
    if mode == "brightness":
        mode = "color"
        print("Mode changed to Color")
    else:
        mode = "brightness"
        print("Mode changed to Brightness")

def rotation_decode(Enc_A):
    if mode == "brightness":
        adjust_brightness()
    elif mode == "color":
        change_color()

def adjust_brightness():
    global brightness
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)

    if (Switch_A == 1) and (Switch_B == 0):
        brightness += bright_res
        print("Increasing Brightness: ", brightness)
        update_brightness()
        wait_for_rotation_end()
    elif (Switch_A == 1) and (Switch_B == 1):
        brightness -= bright_res
        print("Decreasing Brightness: ", brightness)
        update_brightness()
        wait_for_rotation_end()

def change_color():
    global color_index, pixels
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)

    if (Switch_A == 1) and (Switch_B == 0):
        # Cycle to the next color in the wheel
        color_index = (color_index + 1) % len(color_wheel)
        new_color = color_wheel[color_index]
        pixels.fill(new_color)
        print("Changing Color: ", new_color)
        wait_for_rotation_end()
    elif (Switch_A == 1) and (Switch_B == 1):
        # Cycle to the previous color in the wheel
        color_index = (color_index - 1) % len(color_wheel)
        new_color = color_wheel[color_index]
        pixels.fill(new_color)
        print("Changing Color: ", new_color)
        wait_for_rotation_end()

def update_brightness():
    global brightness, pixels
    # Clamp brightness to be between 0 and 1
    brightness = max(0, min(1, brightness))
    pixels.brightness = brightness
    pixels.show()

def wait_for_rotation_end():
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
    while Switch_A == 1 or Switch_B == 1:
        Switch_A = GPIO.input(Enc_A)
        Switch_B = GPIO.input(Enc_B)

def main():
    try:
        init()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
