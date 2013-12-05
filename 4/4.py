#!/usr/bin/python2
# -*- coding: utf-8

#stubb for project:  4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#decremendown from max, find a palindrome, then good!

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
            print n[0], n[1], 'True'
            return True
        else:
            print n[0], n[1], 'False'
            return False

    #if we have more than two numbers, compare the substring..
    #if outer numbers are equal that is.
    if len(n) > 2 and n[0] == n[-1]:
        subs = n[1:-1]
        print subs
        if is_palindrome(subs):
            return True
        else:
            return False

    else:
        return False


# you know what, i bet it's because 997799 is a prime... so can't be split into two ints.
# or at least, cannot be split into two, 3-digit nums
# i need to get a case of all 3 digits * all 3 digits
# could make a function that tests if number can be factored into two 3 digit nums
# or could iterate through different combinations of 3 digit num multiples.

def main():
    x = maxnum
    lim = 99*99
    while x > lim:
        if is_palindrome(x):
            print x
            break

        else:
            #print x
            x -= 1

#need to have a case for when there are two
#print is_palindrome(9 9 79 9 9)
main()


