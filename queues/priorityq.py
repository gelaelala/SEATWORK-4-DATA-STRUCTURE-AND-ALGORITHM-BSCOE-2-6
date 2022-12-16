from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2 
NEUTRAL = 1

messages = PriorityQueue ()
messages.enqueue_with_priority (IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority (NEUTRAL, "Radion station tuned in")