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


def get_list(num):
    def break_number(n):
        lst = []
        a = n - 1
        while (n - a) < a:
            b = n - a
            lst.append((a, b))
            a -= 1

        return lst

    #our number to the left:
    p = num - 1

    while p > num/4:
        b = num - p
        x = break_number(b)
        for each in x:
            if is_series(each[1], each[0], p):
                if is_triplet(each[1], each[0], p):
                    print 'a:', each[1], 'b:', each[0], 'c:', p
                    print 'product: ', each[1] * each[0] * p

        p -= 1


get_list(12)
get_list(1000)
