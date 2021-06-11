""" Python Script to create a stack and perform various operations on it """

# Write your code from here

# Demo using list

##stack_01 = []
##
##stack_01.append('a')
##stack_01.append('b')
##stack_01.append('c')
##
##print('Stack = ', stack_01)
##
##
##print('\nElements poped from stack:')
##print(stack_01.pop())
##print(stack_01.pop())
##print(stack_01.pop())
##
##print('\nStack after elements are poped:', stack_01)



# Demo using a linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        current = self.head.next
        output = ""
        while current:
            output += str(current.value) + "->"
            current = current.next
        return output[:-3]

    def getSize(self):
        return self.size
	
    def isEmpty(self):
        return self.size == 0
	
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
	
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

stack_02 = Stack()
for i in range(10):
	stack_02.push(i)
print("Elements of the stack are ...", stack_02)

for _ in range(3):
	remove = stack_02.pop()
	print("Elment popped : ", remove)
print("Elements of the stack after popping ...", stack_02)

