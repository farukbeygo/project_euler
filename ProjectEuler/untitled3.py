# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:52:56 2022

@author: beygo
"""

"""
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome_list = []
hund_to_tou = []
div_palindrome = []

for n in range(100,1000):
    hund_to_tou.append(n)

#we need to calculate the palindrome number between 10000 to 1000000, 
#since 100*100 is 100000, and 1000*1000 is 1000000

#i will divide my loop by 2, like 10000 to 100000, and 100000 to 1000000
for num in range(10000, 100000):
    if (str(num)[0] == str(num)[4]) and (str(num)[1] == str(num)[3]):
        palindrome_list.append(num)

for numb in range(100000, 1000000):
    if (str(numb)[0] == str(numb)[5]) and (str(numb)[1] == str(numb)[4]) and (str(numb)[2] == str(numb)[3]):
        palindrome_list.append(numb)

#it is very unefficient code, i know but it works
for palindrome in palindrome_list:
    for i in hund_to_tou:
        if palindrome not in div_palindrome:  
            for j in hund_to_tou:
                if i*j == palindrome:
                    div_palindrome.append(palindrome)
                    
print(max(div_palindrome))
    

