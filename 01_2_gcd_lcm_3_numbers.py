""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here

gcd of n numbers = gcd of (gcd of n-1 numbers, nth number)

def gcd(n_1, n_2):
    if n_1 == 0:
        return n_2
    return gcd(n_2 % n_1, n_1)

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

gcd_2 = gcd(number_1, number_2)

result_gcd = gcd(gcd_2, number_3)
print("GCD of the three numbers is ", result_gcd)

lcm_2 = (number_1 * number_2) // gcd_2

print("LCM of the three numbers is ", (lcm_2 * number_3)//gcd(number_3, lcm_2))

##Output:
##Enter first number: 10
##Enter second number: 20
##Enter third number: 30
##GCD of the three numbers is  10
##LCM of the three numbers is  60
