from collections import deque
from heapq import heappop, heappush
from itertools import count

class Queue:
    def __init__ (self, *elements):
        self._elements = deque (elements)

    def __len__ (self):
        return len (self._elements)

    def __iter__ (self):
        while len (self) > 0:
            yield self.dequeue ()

    def enqueue (self, element):
        self._elements.append (element)

    def dequeue (self):
        return self._elements.popleft ()

class Stack (Queue):
    def dequeue (self):
        return self._elements.pop ()

class PriorityQueue:
    def __init__ (self):
        self._elements = []

    def enqueue_with_priority (self, priority, value):
        heappush (self._elements, (-priority, value))

    def dequeue (self):
        return heappop (self._elements) [1]
