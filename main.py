from queue import Queue
from threading import Thread
from producer import producer
from consumer import consumer
from resolution import *

import helpers


if __name__ == "__main__":

    mode = None
    while mode is not FULL_HD_MODE and mode is not ULTRA_WIDE_MODE:
        mode = input("Choose which mode to launch.\n"
                + "(NOTE: Choose the monitor that is your MAIN display on Windows OS.)\n"
                + "[f] Full HD    : (1920 x 1080)\n"
                + "[u] Ultra Wide : (5120 x 1440)")

    helpers.find_and_save_monitor_by_mode(mode)

    print(f"monitor_index: {helpers.monitor_index}")
    print(f"monitor_shape: {helpers.monitor_shape}")

    read_box = RESOLUTION_CONFIG[mode]["read_box"]
    write_box = RESOLUTION_CONFIG[mode]["write_box"]

    queue = Queue()

    producer_thread = Thread(target=producer, args=(queue,read_box))
    producer_thread.daemon = True
    producer_thread.start()

    consumer(queue, write_box)