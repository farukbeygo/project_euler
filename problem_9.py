"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# now write a function that return are given numbers pythagorean
def is_pyth(a, b, c):
    if ((a**2 + b**2) == c**2):
        return True
    return False

# now write a loop to find pythagoreans
in_loop = True
for num_1 in range(1, 1000):
    for num_2 in range(1, 1000):
        num_3 = 1000 -num_2 -num_1
        if (is_pyth(num_1, num_2, num_3)):
            print(num_1 * num_2 * num_3)
            in_loop = False
    if in_loop == False:
        break
