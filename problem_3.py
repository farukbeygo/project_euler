"""
"The following problem is taken from Project Euler."

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

# I will write function that return primeFactors of the given number
def Factor(x):
    factor_list = []
    for factor in range(2, round(sqrt(x))):
        if x%factor == 0:
            factor_list.append(factor)
    return factor_list

# NHere is another function that return primeFactorList of the given number
def primeFactor(x):
    primeFactor_list = []
    for num in Factor(x):
        flag = True
        for prime in range(2, round(sqrt(num))):
            if num%prime == 0:
                flag = False
                break
        if flag:
            primeFactor_list.append(num)
    return primeFactor_list
