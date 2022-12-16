from queues import Queue

fifo = Queue ("1st", "2nd", "3rd")
print (len(fifo))

for element in fifo:
    print (element)

print (len(fifo))