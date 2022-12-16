import argparse
from queue import LifoQueue, PriorityQueue, Queue

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