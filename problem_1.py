"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# I'll write a function that return sum of multiples of 3 or 5 for the given number

def mul_sum(x):
    # I will calculate the sum with a loop
    mulSum = 0
    n3 = 3
    n5 = 5
    n15 = 15
    while x>n3:
        mulSum+=n3
        n3+=3
    while x>n5:
        mulSum+=n5
        n5+=5
    while x>n15:
        mulSum-=n15
        n15+=15
    return mulSum
