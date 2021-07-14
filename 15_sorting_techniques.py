""" Python Script to implement various sorting techniques: 
    - Insertion sort
    - Selection Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort
    - Heap Sort
    [Compare with Python's Built-In Sorting Functions also]  """

# Write your code from here

# Python program for implementation of Insertion Sort

def insertion_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        print("Iteration - ", i , "Input list = ", list_of_numbers)
        current_element = list_of_numbers[i]
        predecessor_index = i -1
        while (predecessor_index >=0) and (current_element < list_of_numbers[predecessor_index]):
            list_of_numbers[predecessor_index+1]=list_of_numbers[predecessor_index]
            predecessor_index -= 1
        list_of_numbers[predecessor_index+1] = current_element




# Python program for implementation of Selection Sort


def selection_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        print("Iteration - ", i+1 , "Input list = ", list_of_numbers)
        minimum_value_index = i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[minimum_value_index] > list_of_numbers[j]:
                minimum_value_index = j
        list_of_numbers[i], list_of_numbers[minimum_value_index] = list_of_numbers[minimum_value_index], list_of_numbers[i]



# Python program for implementation of Bubble Sort

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        print("Iteration - ", i+1 , "Input list = ", list_of_numbers)
        for j in range(0, len(list_of_numbers)-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1] :
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
            


# Python program for implementation of Quicksort Sort
def partition(list_of_numbers, low, high):
    i = low	 # index of smaller element
    pivot = list_of_numbers[high]	 # pivot
    for j in range(low, high):
        if list_of_numbers[j] <= pivot:
            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
            i = i+1
    list_of_numbers[i], list_of_numbers[high] = list_of_numbers[high], list_of_numbers[i]
    return i


def quick_sort(list_of_numbers, low, high):
    global counter
    print("Iteration - ", counter , "Input list = ",list_of_numbers)
    counter = counter + 1
    if low < high:
        partition_index = partition(list_of_numbers, low, high)
        quick_sort(list_of_numbers, low, partition_index - 1)
        quick_sort(list_of_numbers, partition_index + 1, high)
        #print(list_of_numbers)


# Python program for implementation of MergeSort
def merge_sort(list_of_numbers):
    global counter
    print("Iteration - ", counter , "Input list = ",list_of_numbers)
    counter = counter + 1
    if len(list_of_numbers) > 1:
        middle_index = len(list_of_numbers)//2
        left_sublist = list_of_numbers[:middle_index]
        right_sublist = list_of_numbers[middle_index:]
        merge_sort(left_sublist)
        merge_sort(right_sublist)

        i = j = k = 0
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] < right_sublist[j]:
                list_of_numbers[k] = left_sublist[i]
                i += 1
            else:
                list_of_numbers[k] = right_sublist[j]
                j += 1
            k += 1
        while i < len(left_sublist):
            list_of_numbers[k] = left_sublist[i]
            i += 1
            k += 1
        while j < len(right_sublist):
            list_of_numbers[k] = right_sublist[j]
            j += 1
            k += 1


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    global counter
    print("Iteration - ", counter , "Input list = ",arr)
    counter = counter + 1
    largest = i # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


list_of_numbers = [19, 1, 11, 13, 5, 6, 9]
counter=1            

##insertion_sort(list_of_numbers)
##selection_sort(list_of_numbers)
##bubble_sort(list_of_numbers)
##quick_sort(list_of_numbers, 0, len(list_of_numbers)-1)
##merge_sort(list_of_numbers)
heap_sort(list_of_numbers)


print ("Elements after sorting: ", list_of_numbers)


##Output of Insertion Sort
##
##Iteration -  1 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  2 Input list =  [1, 19, 11, 13, 5, 6, 9]
##Iteration -  3 Input list =  [1, 11, 19, 13, 5, 6, 9]
##Iteration -  4 Input list =  [1, 11, 13, 19, 5, 6, 9]
##Iteration -  5 Input list =  [1, 5, 11, 13, 19, 6, 9]
##Iteration -  6 Input list =  [1, 5, 6, 11, 13, 19, 9]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Selection Sort
##Iteration -  0 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  1 Input list =  [1, 19, 11, 13, 5, 6, 9]
##Iteration -  2 Input list =  [1, 5, 11, 13, 19, 6, 9]
##Iteration -  3 Input list =  [1, 5, 6, 13, 19, 11, 9]
##Iteration -  4 Input list =  [1, 5, 6, 9, 19, 11, 13]
##Iteration -  5 Input list =  [1, 5, 6, 9, 11, 19, 13]
##Iteration -  6 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Bubble Sort
##Iteration -  0 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  1 Input list =  [1, 11, 13, 5, 6, 9, 19]
##Iteration -  2 Input list =  [1, 11, 5, 6, 9, 13, 19]
##Iteration -  3 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Iteration -  4 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Iteration -  5 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Quick Sort
##[19, 1, 11, 13, 5, 6, 9]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 11, 13, 19]
##[1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]
