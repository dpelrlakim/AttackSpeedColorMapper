from mss import mss
from resolution import *

monitor_index = None
monitor_shape = None

# Will set global variables `monitor_index` and `monitor_shape` based on user input on which is their main screen.
# Meant to be called only once
def find_and_save_monitor_by_mode(mode: str):
    with mss() as sct:
        for i, monitor in enumerate(sct.monitors):
            (width, height) = RESOLUTION_CONFIG[mode]["resolution"]
            if monitor["width"] == width and monitor["height"] == height:
                global monitor_index, monitor_shape
                monitor_index = i
                monitor_shape = monitor
                return

