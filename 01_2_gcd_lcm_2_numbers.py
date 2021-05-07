""" Python Script to find GCD and LCM of 2 numbers """
import time
# Write your code from here

# This uses recursion function

# product of the two numbers = gcd * lcm

def gcd(n_1, n_2):
    if n_1 == 0:
        return n_2
    return gcd(n_2 % n_1, n_1)

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter Second number: "))

start_time = time.time()
result_gcd = gcd(number_1, number_2)
print("GCD of the two numbers is ", result_gcd)

print("LCM of the two numbers is ", (number_1 * number_2)//result_gcd)

end_time = time.time()

print("Execution time is ", end_time - start_time)

##Output:
##Enter first number: 100
##Enter Second number: 25
##GCD of the two numbers is  25
##LCM of the two numbers is  100.0

##Enter first number: 10
##Enter Second number: 20
##GCD of the two numbers is  10
##LCM of the two numbers is  20.0
##Execution time is  0.017895936965942383


##Enter first number: 123456789
##Enter Second number: 987654321
##GCD of the two numbers is  9
##LCM of the two numbers is  1.354807012362614e+16
##Execution time is  0.022659778594970703


##Enter first number: 123456789
##Enter Second number: 987654321
##GCD of the two numbers is  9
##LCM of the two numbers is  13548070123626141
##Execution time is  0.0284121036529541
