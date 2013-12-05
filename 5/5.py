#stubb for project:  5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#testing each number for div by 1-20 seems a waste. if something is divisible by 4 & 5m then it's divisible by 20 too.

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




main()



