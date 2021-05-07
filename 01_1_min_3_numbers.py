""" Python Script to find minimum among three numbers """
# Write your code from here

import time

print("Provide three numbers...")
number_1 = int(input("Enter First number: "))
number_2 = int(input("Enter Second number: "))
number_3 = int(input("Enter Third number: "))

start_time = time.time()

print("Minimum of the given three numbers is ", min(min(number_1, number_2), number_3))

end_time = time.time()

print("Execution time taken by the program is ", end_time - start_time)

##Number of Cases = 6
##1,2,3
##1,3,2
##2,1,3
##2,3,1
##3,1,2
##3,2,1

##Provide three numbers...
##Enter First number: 6
##Enter Second number: 8
##Enter Third number: 2
##Minimum of the given three numbers is  2
##Execution time taken by the program is  0.008289337158203125


##Provide three numbers...
##Enter First number: 9
##Enter Second number: 2
##Enter Third number: 6
##Minimum of the given three numbers is  2
##Execution time taken by the program is  0.02679896354675293
