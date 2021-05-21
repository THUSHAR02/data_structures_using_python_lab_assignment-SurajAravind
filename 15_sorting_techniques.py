""" Python Script to implement various sorting techniques: 
    - Insertion sort
    - Selection Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort 
    [Compare with Python's Built-In Sorting Functions also]  """

# Write your code from here

# Python program for implementation of Insertion Sort

def insertion_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        current_element = list_of_numbers[i]
        predecessor_index = i -1
        while (predecessor_index >=0) and (current_element < list_of_numbers[predecessor_index]):
            list_of_numbers[predecessor_index+1]=list_of_numbers[predecessor_index]
            predecessor_index -= 1
        list_of_numbers[predecessor_index+1] = current_element




# Python program for implementation of Selection Sort


def selection_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        minimum_value_index = i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[minimum_value_index] > list_of_numbers[j]:
                minimum_value_index = j
        list_of_numbers[i], list_of_numbers[minimum_value_index] = list_of_numbers[minimum_value_index], list_of_numbers[i]



# Python program for implementation of Bubble Sort

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        for j in range(0, len(list_of_numbers)-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1] :
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]





list_of_numbers = [19, 1, 11, 13, 5, 6, 9]

##insertion_sort(list_of_numbers)
##selection_sort(list_of_numbers)
bubble_sort(list_of_numbers)


print ("Elements after sorting: ", list_of_numbers)
