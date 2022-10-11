# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:49:35 2022

@author: beygo
"""

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

prime_list = [ 2, 3, 5, 7, 11, 13]
i = 13

while max(prime_list)<2000000:
    i+=1
    flag = True
    for num in range(2, round(math.sqrt(i)+1)):
        if i%num == 0:
            flag = False
            break
    if flag:
        prime_list.append(i)

print(sum(prime_list)-max(prime_list))