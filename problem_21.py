"""
"The following problem is taken from Project Euler."

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# I will write a funtion that return sum of proper divisors of given number
def div_sum(x):
    div_sum = 0
    for divisor in range(1, (round(x/2) + 1)):
        if x%divisor == 0:
            div_sum+=divisor
    return div_sum

# now we can write a function that can check whether amicable or not that given numbers
def is_amicable(x, y):
    if (div_sum(x) == y and div_sum(y) == x):
        return True
    else:
        return False
    
# now we can check which of the numbers are amicable under 10000
amicable_list = []
for i in range(1,10000):
    if (i not in amicable_list): 
        for j in range(1,10000):
            if (is_amicable(i, j)):
                amicable_list.append(i)
                amicable_list.append(j)
amicable_sum = sum(amicable_list)
