from mss import mss

import pygame
import pytesseract
import colorsys
import numpy as np


# red → yellow → green → cyan → blue → magenta → red
def speed_to_rgb(attack_speed: float):

    # Normalize attack speed to range [0, 1]
    hue = min(max(attack_speed, 0), 2.5) / 2.5  # Assume max AS is 2.5

    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Full saturation and brightness

    # Scale RGB from [0, 1] to [0, 255]
    return (int(r * 255), int(g * 255), int(b * 255))


def rgb_to_hex(r: int, g: int, b: int):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


plus = True
def translate_speed_to_color():

    screenshot = None

    with mss() as sct:

        # [0] is the union virtual monitor. so indiv monitors index from 1.
        monitor = sct.monitors[1]

        region = { # for the ultra wide monitor
            "top": monitor["top"] + 1375,
            "left": monitor["left"] + 2020,
            "width": 74,
            "height": 25,
        }

        sct.grab(region)

    # 1) capture portion of screen to extract image of attack speed
        screenshot = np.array(sct.grab(region))
    
    if not screenshot.any():
        return

    # 2) use OCR to save this data as string (eventually float)
    # about the psm 6 stuff: https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html#page-segmentation-method
    extracted_text = pytesseract.image_to_string(screenshot, config="--psm 6 -c tessedit_char_whitelist=0123456789.").strip()

    try:
        attack_speed = float(extracted_text)

    # ValueError: could not convert string to float: '.\n4'
    # TypeError: float() argument must be a string or a real number, not 'NoneType'
    except (ValueError, TypeError):
        return
    
    # 3) convert attack speed from float to 
    (r, g, b) = speed_to_rgb(attack_speed)

    if plus:
        print(f"|\\ Attack Speed: {attack_speed}")
    else:
        print(f"|/ Attack Speed: {attack_speed}")
    plus = not plus

    # 4) update pygame screen by changing its colour
    screen.fill(rgb_to_hex(r, g, b))
    pygame.display.update()


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    translate_speed_to_color()
    clock.tick(10)  # 10 FPS

pygame.quit()