""" Python Script to create a queue and perform various operations on it """

# Write your code from here

##from queue import Queue
##
##queue_01 = Queue(maxsize = 3)
##
##print("Number of elements in the queue: ", queue_01.qsize())
##
### Adding of element to queue
##queue_01.put('a')
##print("Number of elements in the queue: ", queue_01.qsize())
##queue_01.put('b')
##print("Number of elements in the queue: ", queue_01.qsize())
##queue_01.put('c')
##print("Number of elements in the queue: ", queue_01.qsize())
##
##queue_01.put('d')  # if we insert extra items into the queue, the process gets blocked
##
##
##print("\nFull: ", queue_01.full())


# Removing element from queue
##print("\nElements dequeued from the queue")
##print(queue_01.get())
##print(queue_01.get())
##print(queue_01.get())

# Return Boolean for Empty
# Queue
#print("\nEmpty: ", queue_01.empty())
##
##queue_01.put(1)
##print("\nEmpty: ", queue_01.empty())
##print("Full: ", queue_01.full())



# Priority Queue

##from queue import PriorityQueue
##
##queue_02 = PriorityQueue()
##
### insert into queue
##queue_02.put(("Ara", 'a'))
##queue_02.put(("b", 'b'))
##queue_02.put(("Abc", 'c'))
##queue_02.put(("d", 'd'))
##queue_02.put(("e", 'e'))
##
###print("Prioiry Queue : ", queue_02)
##print('Number of items in queue :', queue_02.qsize())

#for item in queue_02:
#    print(item)

##print(queue_02.get())


##import collections
# Create a deque
##queue_03 = collections.deque(["122010322001","122010322002","122010322003"])
##print (queue_03)
##
##print("Adding to the right: ")
##queue_03.append("122010322004")
##print (queue_03)
##
##print("Adding to the left: ")
##queue_03.appendleft("122010322005")
##print (queue_03)
##
##print("Removing from the right: ")
##queue_03.pop()
##print (queue_03)
##
##print("Removing from the left: ")
##queue_03.popleft()
##print (queue_03)
##
##print("Reversing the deque: ")
##queue_03.reverse()
##print (queue_03)



# Producer - Consumer Problem

from queue import Queue
from threading import Thread
import time
import random

queue_elements = Queue(maxsize = 2)

class Producer_thread(Thread):
    def run(self):
        nums = range(5) #Will create the list [0, 1, 2, 3, 4]
        global queue_elements
        while True:
            num = random.choice(nums) #Selects a random number from list [0, 1, 2, 3, 4]
            queue_elements.put(num)
            print("Produced: ", num)
            time.sleep(1)


class Consumer_thread(Thread):
    def run(self):
        global queue_elements
        while True:
            print("Consumed: ", queue_elements.get())
            time.sleep(3)


Producer_thread().start()
Consumer_thread().start()

