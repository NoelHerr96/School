#!/usr/bin/env python
from random import *
import sys


def gcd(a, b):
    if a < 0 or b < 0:
        sys.exit("\n Integers a, b cannot be negative!\n")
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    while b > 0:
        return gcd(b, a % b)


def fast_power(base, power, MOD):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD
        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD
    return result


def testprimality2(n, trial):
    smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                   41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n < 100 and n in smallprimes:
        return True
    for prime in smallprimes:
        if n % prime == 0:
            return False
    while trial > 0:
        a = randint(1, n)
        # fast_power is the same as the built-in function pow()
        if gcd(a, n) > 1 or fast_power(a, n - 1, n) != 1:
            return False
        trial -= 1
    return True


# n, trial=int(sys.argv[1]), int(sys.argv[2])
# print("{} is a prime: {}".format(n, testprimality(n, trial)))

bits = 1028
trial = 5
n = randint(1 << (bits - 1), 1 << bits)
while not testprimality2(n, trial):
    n = randint(1 << (bits - 1), 1 << bits)
print("{} is a prime: {}\n".format(n, testprimality2(n, trial)))
