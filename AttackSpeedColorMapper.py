from mss import mss
from PIL import Image

import pytesseract
import tkinter
import colorsys

# 캡처 영역의 화면을 가져온다.
import cv2
import numpy as np

DEBUG_MODE = False

# red → yellow → green → cyan → blue → magenta → red
def map_to_color_hsv(attack_speed):
    # Normalize attack speed to range [0, 1]
    hue = min(max(attack_speed, 0), 2.5) / 2.5  # Assume max AS is 2.5
    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Full saturation and brightness
    # Scale RGB from [0, 1] to [0, 255]
    return (int(r * 255), int(g * 255), int(b * 255))


def on_key_press(event):
    if event.char == 'q':
        print("q pressed -- exiting...")
        window.quit()

def create_window():
    root = tkinter.Tk()
    root.title("AttackSpeedColorMapper")
    root.geometry("800x600")
    root.config(bg='black')  # Initial background color
    root.bind('<KeyPress>', on_key_press)
    return root

def update_color(window, color):
    window.config(bg=color)
    window.update()  # Force an update to the window

window = create_window()

# Initialize MSS
with mss() as sct:
    while True:
        # Capture the entire screen
        monitor = sct.monitors[1]  # Change if using multiple monitors

        region = {
            "top": monitor["top"] + 1375,
            "left": monitor["left"] + 2020,
            "width": 74,
            "height": 25,
        }
        screenshot = np.array(sct.grab(region))

        if DEBUG_MODE:
            # [DEBUG] Display the live screen
            cv2.imshow("Screen Preview", cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR))

            # [DEBUG] Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # "--psm 6" means "single block of text"
        extracted_text = pytesseract.image_to_string(screenshot, config='--psm 6 digits')
        
        attack_speed = ''.join(filter(str.isdigit, extracted_text))
        if not attack_speed:
            continue
        
        attack_speed = float(attack_speed) / 100
        color = map_to_color_hsv(attack_speed)
        update_color(window, f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')

        



cv2.destroyAllWindows()

# OCR로 숫자를 읽는다.
# 숫자에 맞는 색상을 계산한다.
# 색상을 GUI에 표시한다.
# 반복한다.