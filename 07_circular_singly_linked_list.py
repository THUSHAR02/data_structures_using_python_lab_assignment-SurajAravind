""" Python Script to create a Circular singly linked list for adding and 
deleting a Node. """

# Write your code from here

#Version_01
#Use any visualization tool to understand the flow of execution

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None


my_linked_list = Linked_List()
  
def linkedlist_traversal(head_node):
    count = 0
    temporary_node = head_node
    while True:
        print(temporary_node.data)
        temporary_node = temporary_node.next
        count += 1
        if temporary_node == head_node:
            break
    print("Number of elements in the linked list is : ", count)
    

# Create a circular linked list with 10 nodes for demo purpose
node_elements = [5,4,3,2,1,6,7,8,9,0]

for i in range(10):
    new_node = Node(node_elements[i])
    if my_linked_list.head==None:  # Inserting first element
        my_linked_list.head = new_node
    else:
        temporary_node = my_linked_list.head
        while temporary_node.next != None:
            temporary_node = temporary_node.next
        temporary_node.next = new_node
new_node.next = my_linked_list.head    

linkedlist_traversal(my_linked_list.head)


# Delete an element at a particular location

##position = int(input("Enter at what position U want the element to be deleted: "))
##temporary_node = my_linked_list.head
##
##for i in range(position-2):
##    temporary_node = temporary_node.next
##temporary_node.next = temporary_node.next.next
##
##linkedlist_traversal(my_linked_list.head)

# Insert element at a particular location

location = int(input("Enter the position or location U want to insert a new node: "))
# case where the location value is greater than the size of the linked list is not considered here
element_1 = input("Enter a number to be inserted at a particular location: ")
new_node = Node(element_1)
temporary_node = my_linked_list.head

for i in range(location-1):
    temporary_node = temporary_node.next

new_node.next = temporary_node.next
temporary_node.next = new_node

linkedlist_traversal(my_linked_list.head)
    


