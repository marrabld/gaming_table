from gpiozero import Button
from signal import pause
import board
import neopixel

# Rotary Encoder Pins
enc_a = Button(21, pull_up=True)  # Assuming pull-up resistor
enc_b = Button(16, pull_up=True)  # Assuming pull-up resistor

# Push Button Setup
push = Button(20, pull_up=True)

# NeoPixel Setup
npins = 240 * 3  # Adjusted for clarity
brightness = 0.1  # Starting brightness
mode = "brightness"  # Modes: "brightness" or "color"
color_index = 0  # Index to keep track of the current color
bright_res = 0.025  # Brightness resolution

# Initialize the NeoPixel
pixels = neopixel.NeoPixel(board.D18, npins, brightness=brightness)

# Define a color wheel
color_wheel = [
    (255, 255, 255), (255, 0, 0), (255, 64, 0), (255, 128, 0), (255, 191, 0),
    (255, 255, 0), (191, 255, 0), (128, 255, 0), (64, 255, 0), (0, 255, 64),
    (0, 255, 128), (0, 255, 191), (0, 255, 255), (0, 191, 255), (0, 128, 255),
    (0, 64, 255), (64, 0, 255), (128, 0, 255), (191, 0, 255), (255, 0, 255),
    (255, 0, 191), (255, 0, 128), (255, 0, 64), (0, 0, 0)
]

def toggle_mode():
    global mode
    if mode == "brightness":
        mode = "color"
        print("Mode changed to Color")
    else:
        mode = "brightness"
        print("Mode changed to Brightness")

def rotation_decode():
    global mode, color_index, brightness
    if mode == "brightness":
        adjust_brightness()
    elif mode == "color":
        change_color()

def adjust_brightness():
    global brightness, pixels
    if enc_a.is_pressed and not enc_b.is_pressed:
        brightness += bright_res
        if brightness > 1: brightness = 1
    elif enc_a.is_pressed and enc_b.is_pressed:
        brightness -= bright_res
        if brightness < 0: brightness = 0
    print(f"Current Brightness: {brightness}")
    pixels.brightness = brightness
    pixels.show()

def change_color():
    global color_index, pixels
    if enc_a.is_pressed and not enc_b.is_pressed:
        color_index = (color_index + 1) % len(color_wheel)
    elif enc_a.is_pressed and enc_b.is_pressed:
        color_index = (color_index - 1) % len(color_wheel)
    new_color = color_wheel[color_index]
    pixels.fill(new_color)
    print(f"Changed Color to: {new_color}")

# Setup event handlers
push.when_pressed = toggle_mode
enc_a.when_pressed = rotation_decode  # Adjust as needed for proper handling

def main():
    print("Rotary Encoder and Button Test Program")
    try:
        pixels.fill(color_wheel[0])  # Start with the first color in the wheel
        pause()  # Keep the script running to listen for button presses
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        print("Cleaning up GPIO")

if __name__ == '__main__':
    main()
