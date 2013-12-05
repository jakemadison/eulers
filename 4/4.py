#!/usr/bin/python
# -*- coding: utf-8
#stubb for project:  4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#decremendown from max, find a palindrome, does it have good factors? then good!

maxnum = 999*999


#gimmie a number, I'll tell you if it's a palindrome:
def is_palindrome(n):
    n = str(n)

    #if we only have one number, true by default
    if len(n) == 1:
        return True

    #if we only have two numbers, true if they are equal
    if len(n) == 2:
        if n[0] == n[-1]:
            return True
        else:
            return False

    #if we have more than two numbers, compare the substring..
    #if outer numbers are equal that is.
    if len(n) > 2 and n[0] == n[-1]:
        subs = n[1:-1]
        #print subs
        if is_palindrome(subs):
            return True
        else:
            return False

    else:
        return False


#give me a number, i'll tell you if it can be broken into 2, 3-digit factors
def is_trip_factor(n):

    n = int(n)
    fac = 999

    while fac > 99:
        if n % fac == 0:
            if len(str(n/fac)) == 3:
                print '::', fac, (n/fac)
                return True

        fac -= 1

    return False


def main():
    x = maxnum
    lim = 99*99
    while x > lim:
        if is_palindrome(x):
            print x
            if is_trip_factor(x):
                print '---------->', x
                break
            else:
                x -= 1
        else:
            x -= 1


main()


