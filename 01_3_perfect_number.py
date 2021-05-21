""" Python Script to check whether a given number is perfect  """

# Write your code from here


##In number theory, a perfect number is a positive integer that is equal to the
##sum of its proper positive divisors, that is, the sum of its positive divisors
##excluding the number itself (also known as its aliquot sum).
##
##Equivalently, a perfect number is a number that is half the sum of all of its
##positive divisors (including itself).
##
##Example : The first perfect number is 6, because 1, 2, and 3 are its proper
##positive divisors, and 1 + 2 + 3 = 6.
##Equivalently, the number 6 is equal to half the sum of all its positive divisors:
##( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
##This is followed by the perfect numbers 496 and 8128.


##number_01 = int(input("Enter a number to find out whether it is perfect or not: "))
##
##sum_of_divisors = 0
##
##for x in range(1, number_01):
##    if number_01 % x == 0:
##        sum_of_divisors += x
##if (sum_of_divisors == number_01):
##    print("The given number is perfect")
##else:
##    print("The given number is not perfect")

##Output:
##
##Enter a number to find out whether it is perfect or not: 6
##The given number is perfect

##Enter a number to find out whether it is perfect or not: 10
##The given number is not perfect


number_02 = 28

def factors(number_02):
    for x in range(1, number_02):
        if number_02 % x == 0:
            yield x

print(factors(number_02))

for i in factors(number_02):
    print(i)
