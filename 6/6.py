#!/usr/bin/python2
# -*- coding: utf-8
#stubb for project:  6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#seems like a pretty good candidate for generator functions..


def sumofsquares(maxm):

    def gen_squares():
        x = 1
        while True:
            yield x ** 2
            x += 1

    gen = gen_squares()
    total = 0

    while maxm:
        total += next(gen)
        maxm -= 1

    return total


def squareofsums(maxm):

    def gen_sums():
        x = 1
        t = 0

        while True:
            t += x
            x += 1
            yield t ** 2

    gen = gen_sums()

    while maxm:
        x = next(gen)
        maxm -= 1

    return x


a = sumofsquares(100)
b = squareofsums(100)

print b - a