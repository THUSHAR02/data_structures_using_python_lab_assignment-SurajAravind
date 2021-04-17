""" Python Script to find minimum among three numbers """

# Write your code from here
print("Provide three numbers...")
number_1 = int(input("Enter First number: "))
number_2 = int(input("Enter Second number: "))
number_3 = int(input("Enter Third number: "))

if (number_1 < number_2) and (number_1 < number_3):
    print("The minimum of the three numbers is : ", number_1)
elif (number_1 >= number_2) and (number_2 <= number_3):
    print("The minimum of the three numbers is : ", number_2)
elif (number_1 >= number_2) and (number_3 <= number_2):
    print("The minimum of the three numbers is : ", number_3)    


##Output
##1_min_3_numbers.py
##Case-1
##Provide three numbers...
##Enter First number: 1
##Enter Second number: 2
##Enter Third number: 3
##The minimum of the three numbers is :  1
##
##case-2
##Provide three numbers...
##Enter First number: 2
##Enter Second number: 3
##Enter Third number: 1
##
##case-3
##Provide three numbers...
##Enter First number: 3
##Enter Second number: 2
##Enter Third number: 1
The minimum of the three numbers is :  1
