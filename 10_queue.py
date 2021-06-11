""" Python Script to create a queue and perform various operations on it """

# Write your code from here

from queue import Queue

queue_01 = Queue(maxsize = 3)

print("Maximum number of elements that can be included into the queue: ", queue_01.qsize())

# Adding of element to queue
queue_01.put('a')
queue_01.put('b')
queue_01.put('c')


print("\nFull: ", queue_01.full())


# Removing element from queue
print("\nElements dequeued from the queue")
print(queue_01.get())
print(queue_01.get())
print(queue_01.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", queue_01.empty())

queue_01.put(1)
print("\nEmpty: ", queue_01.empty())
print("Full: ", queue_01.full())
