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
        print("Iteration - ", i , "Input list = ", list_of_numbers)
        minimum_value_index = i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[minimum_value_index] > list_of_numbers[j]:
                minimum_value_index = j
        list_of_numbers[i], list_of_numbers[minimum_value_index] = list_of_numbers[minimum_value_index], list_of_numbers[i]



# Python program for implementation of Bubble Sort

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        print("Iteration - ", i , "Input list = ", list_of_numbers)
        for j in range(0, len(list_of_numbers)-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1] :
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]





# Python program for implementation of Quicksort Sort

def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


##def quick_sort(list_of_numbers):
##	if len(list_of_numbers) == 1:
##		return list_of_numbers
##	else:
##            low = 0
##            high = len(list_of_numbers - 1)
##            if low < high:
##
##		# pi is partitioning index, arr[p] is now
##		# at right place
##		pivot_element = partition(list_of_numbers, low, high)
##
##		# Separately sort elements before
##		# partition and after partition
##		quickSort(arr, low, pi-1)
##		quickSort(arr, pi+1, high)
##
##
##n = len(arr)
##quickSort(arr, 0, n-1)
##print("Sorted array is:")
##for i in range(n):
##	print("%d" % arr[i]),


list_of_numbers = [19, 1, 11, 13, 5, 6, 9]

##insertion_sort(list_of_numbers)
##selection_sort(list_of_numbers)
bubble_sort(list_of_numbers)
##quick_sort(list_of_numbers)



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
