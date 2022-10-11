# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:07:56 2022

@author: beygo
"""

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def prime_order(x):
    flag = True
    prime_list = [ 2, 3, 5, 7, 11, 13]
    i=13
    if x<6:
        return prime_list[x-1]
    else:
        while len(prime_list)<x:
            i+=1
            flag = True
            for num in range(2, round(math.sqrt(i)+1)):
                if i%num == 0:
                    flag = False
                    break
            if flag:
                prime_list.append(i)
    return max(prime_list)

print(prime_order(10001))
                    
            

