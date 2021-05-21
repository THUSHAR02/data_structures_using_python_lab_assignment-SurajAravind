""" Python script to perform binary search on a list stored in an array """

# Write your code from here

import random
random_data_list = []
for i in range(0,50):
    n = random.randint(1,10000)
    random_data_list.append(n)
random_data_list.sort()
print(random_data_list)

element_to_be_searched = int(input("Enter the integer to be searched: "))
flag = False

while True:
    if len(random_data_list) == 1:
        if random_data_list[0] == element_to_be_searched:
           print("Element Found")
        else:
           print("Element NOT Found")
        break
    middle_element = random_data_list[len(random_data_list) //2]
    if middle_element == element_to_be_searched:
        print("Element Found")
        break
    elif middle_element > element_to_be_searched:
        random_data_list = random_data_list[1:len(random_data_list)//2]
    else:
        random_data_list = random_data_list[len(random_data_list)//2+1:]
