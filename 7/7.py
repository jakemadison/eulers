
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#stubb for project:  7
# hmmmm, seems like another good generatory thing...


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

    while n:
        x = next(gen)
        n -= 1

    print x

get_prime(10001)
print 'done!'
