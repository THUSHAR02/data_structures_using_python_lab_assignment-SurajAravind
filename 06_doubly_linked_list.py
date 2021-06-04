""" Python script to create a doubly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here

#Version_01
#Use any visualization tool to understand the flow of execution

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None


my_linked_list = Doubly_Linked_List()
    

def linkedlist_traversal(head_node):
    count = 0
    temporary_node = head_node
    while temporary_node != None:
        print(temporary_node.data, end = "->")
        previous_node = temporary_node.prev
        temporary_node = temporary_node.next
        #previous_node = temporary_node.prev
        count += 1
    print("\n Number of elements in the linked list is : ", count)
    print("Print data in reverse direction...")
    previous_node = previous_node.next
    while previous_node != None:
        print(previous_node.data, end = "->")
        previous_node = previous_node.prev
    

def linkedlist_search(head_node, element):
    temporary_node = head_node
    flag = False
    while temporary_node != None:
        if temporary_node.data == element:
            flag = True
            print("Element found")
            break
        temporary_node = temporary_node.next
    if flag == False:
        print("Element not found")
            



# Create a Doubly linked list with 10 nodes for demo purpose
node_elements = [15,14,13,12,11,16,17,18,19,10]

for i in range(10):
    new_node = Node(node_elements[i])
    if my_linked_list.head==None:  # Inserting first element
        my_linked_list.head = new_node
    else:
        temporary_node = my_linked_list.head
        while temporary_node.next != None:
            temporary_node = temporary_node.next
        temporary_node.next = new_node
        new_node.prev = temporary_node

linkedlist_traversal(my_linked_list.head)



# Insert element at the beginning

##element_1 = input("Enter a number to be inserted at the beginning: ")
##new_node = Node(element_1)
##my_linked_list.head.prev = new_node
##new_node.next = my_linked_list.head
##my_linked_list.head = new_node
##
##
##linkedlist_traversal(my_linked_list.head)


# Insert element at the end

##element_2 = input("Enter a number to be inserted at the end: ")
##new_node = Node(element_2)
##
##temporary_node = my_linked_list.head
##while temporary_node.next != None:
##    temporary_node = temporary_node.next
##new_node.prev = temporary_node
##temporary_node.next = new_node
##
##
##linkedlist_traversal(my_linked_list.head)


# Insert element at a particular location
##position = int(input("Enter at what position U want to insert a node: "))
##element_3 = input("Enter a number to be inserted at a particular position: ")
##new_node = Node(element_3)
##
##temporary_node = my_linked_list.head
##for i in range(position-2):
##    temporary_node = temporary_node.next
##
##temporary_node.next.prev = new_node
##new_node.next = temporary_node.next
##temporary_node.next = new_node
##new_node.prev = temporary_node    
##
##
##linkedlist_traversal(my_linked_list.head)


# Delete element at the beginning

##my_linked_list.head = my_linked_list.head.next
##my_linked_list.head.prev = None
##
##linkedlist_traversal(my_linked_list.head)


# Delete element at the end

##temporary_node = my_linked_list.head
##while temporary_node.next != None:
##    temporary_node = temporary_node.next
##previous_node = temporary_node.prev
##previous_node.next = None
##
##linkedlist_traversal(my_linked_list.head)

# Delete element at a particular location

##position = int(input("Enter at what position U want to delete a node: "))
##
##temporary_node = my_linked_list.head
##for i in range(position-2):
##    temporary_node = temporary_node.next
##
##temporary_node.next = temporary_node.next.next
##temporary_node.next.next.prev = temporary_node
##
##linkedlist_traversal(my_linked_list.head)
