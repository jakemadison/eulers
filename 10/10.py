#stubb for project:  10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# pretty sure this is a good one for our primes generator again.
# kinda slow, but it works!

def get_prime(n):

    #determine if number is prime
    def isPrime(n):
        limit = int(n ** 0.5)+1
        for num in range(2, limit):
            if n % num == 0:
                return False

        return True

    def gen_primes():
        start = 2
        while True:
            if isPrime(start):
                yield start
            start += 1

    gen = gen_primes()
    total = 0

    while True:
        temp = next(gen)
        if temp < n:
            total += temp

        else:
            print 'done!'
            break
    print total

get_prime(2000000)



