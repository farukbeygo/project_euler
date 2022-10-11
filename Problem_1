"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

#I'll collect all elements 1 to 1000 in a one list
num_list = []

for i in range(1, 1000):
    num_list.append(i)

#now we can take them in a another 3_divisor and 5_divisor lists
divided_3 = []
divided_5 = []
divided_15 = []

for num in num_list:
    if num%3 == 0:
        divided_3.append(num)
    elif num%5 == 0 :
        divided_5.append(num)
    elif num%15 == 0 :
        divided_15.append(num)
    
#now we can calculate the sum
total_sum = sum(divided_3) + sum(divided_5) - sum(divided_15)
print(total_sum)
