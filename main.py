from queue import Queue
from threading import Thread
from producer import producer
from consumer import consumer
from resolution import *
from mss import mss


def find_monitor_by_mode():
    with mss.mss() as sct:
        for i, monitor in enumerate(sct.monitors):
            (width, height) = RESOLUTION_CONFIG[mode]["resolution"]
            if monitor["width"] == width and monitor["height"] == height:
                return monitor, i
    return None, None


if __name__ == "__main__":

    mode = None
    while mode is not FULL_HD_MODE and mode is not ULTRA_WIDE_MODE:
        mode = input("Choose which mode to launch.\n"
                + "[f] Full HD    : (1920 x 1080)\n"
                + "[u] Ultra Wide : (5120 x 1440)")

    read_box = RESOLUTION_CONFIG[mode]["read_box"]
    write_box = RESOLUTION_CONFIG[mode]["write_box"]

    queue = Queue()

    producer_thread = Thread(target=producer, args=(queue,read_box))
    producer_thread.daemon = True
    producer_thread.start()

    consumer(queue, write_box)