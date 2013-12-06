#stubb for project:  5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#testing each number for div by 1-20 seems a waste. if something is divisible by 4 & 5m then it's divisible by 20 too.
# i guess all prime factors of 20 would be the way to go?


#gimmie a number... iterate up to that number yielding primes
#wait, might not work... if a number is divisible by two,
#might not be evenly divisible by 4 eg: 6

# here's one optimization, iterate up by 20., check if divisible by 19 first.
# what about iterating by the multiples of all the primes together that are
# less than the number? eg, all primes below 10: 2 * 3 * 5 * 7 * 9 =


#okay, so this definitely works within a decent amount of time,
#but is not very elegant.  Then again, optimize = it's perfect when it works.
def divTest(n, rn):
    x = rn
    while x > 1:
        if n % x != 0:
            return False
        x -= 1
    return True

start = 20
ran = 20
while not divTest(start, ran):
    start += ran
print start
print 'done!'

#print 'working...'
#print divTest(2520, 10)

#print(2520 / (9 * 8 * 7))




def primes(n):
    yield 1
    yield 2
    yield 3
    x = 4
    while x < n:
        if isPrime(x):
            yield x
            x += 1
        else:
            x += 1


def isPrime(n):
    limit = int(n ** 0.5)+1
    for num in range(2,limit):
        if n % num == 0: return False

    return True








start = 1
r = 10

def is_divisible(n, r):
    for x in xrange(2,r+1):
        print x,
        if n % x == 0:
            print 'true'
        else:
            print 'false'




def main():
    rng = r
    while rng > 0:
        is_divisible(2520, rng)
        rng -= 1


#for y in primes(20):
#    print y

# main()



