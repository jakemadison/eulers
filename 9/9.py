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

# I can't believe this ugly garbage actually worked!!!

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

def get_list(num):
    def break_number(n):
        lst = []
        a = n - 1
        while True:
            # print a
            if (n - a) < a:
                b = n - a
                lst.append((a, b))
                a -= 1
            else:
                break

        return lst

    #our number to the left:
    p = num - 1

    while True:
        if p > num/4:
            b = num - p

            x = []

            x = break_number(b)
            for each in x:
                #print 'result: ', p, each[0], each[1]
                if is_series(each[1], each[0], p):
                    if is_triplet(each[1], each[0], p):
                        print 'a:', each[1], 'b:', each[0], 'c:', p
                        print 'product: ', each[1] * each[0] * p

            p -= 1

        else:
            break


get_list(1000)

#
# print is_triplet(1,2,3)
# print is_triplet(3,4,5)
# print is_triplet(4,5,6)
#
#
# max_total = 1000
#
#
#
# # i could find all of the a < b < c's that are under tt, then test if they are pythagorean triplets.
#
#
# a = 3
# b = 4
#
# c = int(math.sqrt((a ** 2) + (b ** 2)))
#
# temptotal = a + b + c
# print 'temptotal: ', temptotal
#
# print c
#
# c = 5
#
#
