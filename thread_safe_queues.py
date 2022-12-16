import argparse
from queue import LifoQueue, PriorityQueue, Queue
import threading
from random import randint
from time import sleep

QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

PRODUCTS = (
    ":ballon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)

class Worker (threading.Thread):
    def __init__ (self, speed, buffer):
        super().__init__ (daemon = True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0
    
    

def main (args):
    buffer = QUEUE_TYPES [args.queue]()

def parse_args ():
    parser = argparse.ArgumentParser ()
    parser.add_argument ("-q", "--queue", choices = QUEUE_TYPES, default = "fifo")
    parser.add_argument ("-p", "--producers", type = int, default = 3)
    parser.add_argument ("-c", "--consumers", type = int, default = 2)
    parser.add_argument ("-ps", "--producder-speed", type = int, default = 1)
    parser.add_argument ("-cs", "--consumer-speed", type = int, default = 1) 

if __name__ == "__main__":
    try: 
        main(parse_args())
    except KeyboardInterrupt:
        pass