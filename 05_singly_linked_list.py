""" Python script to create a singly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here

#Version_01
#Use any visualization tool to understand the flow of execution

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

first_element = Node(5)
##print("Data in the node is : ", first_element.data)

class Linked_List:
    def __init__(self):
        self.head = None


my_linked_list = Linked_List()
my_linked_list.head = first_element

second_element = Node(9)
my_linked_list.head.next = second_element

##
##print(my_linked_list.head.data)
##
### Insert element at the beginning

element_1 = input("Enter a number to be inserted at the beginning: ")
new_node = Node(element_1)
my_linked_list.head = new_node
new_node.next = first_element
##
### Insert element at the end

element_2 = input("Enter a number to be inserted at the end: ")
new_node = Node(element_2)
temporary_node = my_linked_list.head
while temporary_node.next != None:
    temporary_node = temporary_node.next
temporary_node.next = new_node    
    
### Insert element at a particular location
location = int(input("Enter the position or location U want to insert a new node: "))
# case where the location value is greater than the size of the linked list is not considered here
element_3 = input("Enter a number to be inserted at a particular location: ")
new_node = Node(element_3)
temporary_node = my_linked_list.head

for i in range(location-1):
    temporary_node = temporary_node.next

new_node.next = temporary_node.next
temporary_node.next = new_node
    



