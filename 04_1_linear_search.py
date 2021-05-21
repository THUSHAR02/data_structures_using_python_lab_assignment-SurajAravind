""" Python script to perform linear search in an array. """

# Write your code from here
import sys
##Linear or Sequential Search

##Case - 01

##data = [1,8,3,5]
##element_to_be_searched = int(input("Enter the integer to be searched: "))
##
##flag = False
##
##for x in data:
##    if x == element_to_be_searched :
##        print("Element found")
##        flag = True
##if flag == False:
##    print("Element not found")


##Case - 02

##import random
##random_data_list = []
##for i in range(0,1000):
##    n = random.randint(1,10000)
##    random_data_list.append(n)
##
##print(sys.getsizeof(random_data_list))
##print(random_data_list)
##element_to_be_searched = int(input("Enter the integer to be searched: "))
##flag = False
##
##for x in random_data_list:
##    if x == element_to_be_searched :
##        print("Element found")
##        flag = True
##if flag == False:
##    print("Element not found")

##if element_to_be_searched in random_data_list:
##    print("Element found")
##else:
##    print("Element Not found")

##Case - 03  Using Generator

##import random
##flag = False
##def generate_random_list(number_of_elements):
##    for x in range(1, number_of_elements):
##        random_number = random.randint(1, number_of_elements * 2)
##        yield random_number
##
####print(sys.getsizeof(generate_random_list(1000)))
##generator = generate_random_list(1000)
####
##element_to_be_searched = int(input("Enter the integer to be searched: "))
##for x in generator:
##    #print(x)
##    if x == element_to_be_searched :
##        print("Element found")
##        flag = True
##if flag == False:
##    print("Element not found")
    

##Case - 04  On a sorted list

import random
random_data_list = []
for i in range(0,100):
    n = random.randint(1,10000)
    random_data_list.append(n)

##print(random_data_list)
random_data_list.sort()    
element_to_be_searched = int(input("Enter the integer to be searched: "))
flag = False

for x in random_data_list:
    if x == element_to_be_searched :
        print("Element found")
        flag = True
        break
    if x > element_to_be_searched:
        print("Element NOT found")
        flag = True
        break   
if flag == False:
    print("Element not found")

