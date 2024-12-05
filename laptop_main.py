from queue import Queue
from threading import Thread
from producer import producer
from consumer import consumer
from boxshape import BoxShape


if __name__ == "__main__":

    queue = Queue()

    producer_thread = Thread(target=producer, args=(queue,))
    producer_thread.daemon = True
    producer_thread.start()

    consumer(queue)