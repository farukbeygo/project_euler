# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:22:46 2022

@author: beygo
"""

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

initial_num = 1

pri_list = [2, 3, 5, 7, 11, 13, 17, 19]
num_list = []

for i in range(1, 21):
    num_list.append(i)
for j in pri_list:
    initial_num = initial_num * j

for num in num_list:
    if initial_num%num == 0 :
        pass
    else:
        initial_num = initial_num * num