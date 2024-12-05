import pyautogui

# Get the current position of the mouse
while True:
    x, y = pyautogui.position()
    print(f"Mouse is at ({x}, {y})")