from mss import mss
from queue import Queue
import numpy as np
import colorsys
import pytesseract
import time

import helpers
from boxshape import BoxShape


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


def producer(queue: Queue, boxshape: BoxShape):

    plus = True
    while True:
        
        screenshot = None
        with mss() as sct:

            # [0] is the union virtual monitor. so indiv monitors index from 1.
            monitor = sct.monitors[helpers.monitor_index]

            region = { # for the ultra wide monitor
                "left": monitor["left"] + boxshape.x,
                "top": monitor["top"] + boxshape.y,
                "width": boxshape.width,
                "height": boxshape.height,
            }

        # 1) capture portion of screen to extract image of attack speed
            screenshot = np.array(sct.grab(region))

        # 2) use OCR to save this data as string (eventually float)
        # about the psm 6 stuff: https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html#page-segmentation-method
        extracted_text = pytesseract.image_to_string(screenshot, config="--psm 6 -c tessedit_char_whitelist=0123456789.").strip()

        try:
            attack_speed = float(extracted_text)

        # ValueError: could not convert string to float: '.\n4'
        # TypeError: float() argument must be a string or a real number, not 'NoneType'
        except (ValueError, TypeError) as e:
            continue
        
        # 3) convert attack speed from float to rgb
        (r, g, b) = speed_to_rgb(attack_speed)

        if plus:
            print(f"|\\ Attack Speed: {attack_speed}")
        else:
            print(f"|/ Attack Speed: {attack_speed}")
        plus = not plus

        # 4) pass AS and color data to consumer
        if queue.empty():
            queue.put((attack_speed, (r, g, b)))
        else:  # be nice to the computer
            time.sleep(1)
