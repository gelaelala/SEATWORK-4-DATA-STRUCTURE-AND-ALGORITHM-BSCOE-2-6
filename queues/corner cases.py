from queues import PriorityQueue
from dataclasses import dataclass

@dataclass 
class Message:
    event: str

CRITICAL = 3 
IMPORTANT = 2
NEUTRAL = 1   

wipers = Message ("Windshield wipers turned on")
hazard_lights = Message ("Hazard lights turned on")

print (wipers < hazard_lights)

messages = PriorityQueue ()
messages.enqueue_with_priority (CRITICAL, wipers)
messages.enqueue_with_priority (IMPORTANT, hazard_lights)