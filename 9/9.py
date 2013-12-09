#stubb for project:  9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# need something that iterates through pythagorean triplets...
# okay, so... maybe i should start with c, test if sqrt of c is natural number, then
# if its a and b can be squarerooted also...
#

import math


def is_series(a, b, c):
    if a < b < c:
        return True
    else:
        return False


def is_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False



#okay, so a only ever has to iterate up to total/3 (actually even less than that)
# 12. 10, 1, 1. 9, 2, 1. 8,3,1. 7,4,1. 7,3,2
# right, so essentially, this has to iterate down, recursively branching to get our list
# of a,b,cs that we can then test for is_triplet.



tt = 12
a = 1
b = 2
c = 3

# find all permutations where a+b+c = tt, but a < b < c is true.

# while True:
#     if is_triplet(a, b, c):
#         break
#     else:





print is_triplet(1,2,3)
print is_triplet(3,4,5)
print is_triplet(4,5,6)


max_total = 1000



# i could find all of the a < b < c's that are under tt, then test if they are pythagorean triplets.


a = 3
b = 4

c = int(math.sqrt((a ** 2) + (b ** 2)))

temptotal = a + b + c
print 'temptotal: ', temptotal

print c

c = 5


