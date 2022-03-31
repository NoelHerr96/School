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


def testprimality1(n, trial):
    smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                   41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n < 100 and n in smallprimes:
        return True
    for prime in smallprimes:
        if n % prime == 0:
            return False
    while trial > 0:
        a = randint(1, n)
        if gcd(a, n) > 1 or (a**(n - 1) % n) != 1:
            return False
        trial -= 1
    return True


trial = 5
# bits = 28
# n = randint(1 << (bits - 1), 1 << bits)
# print("{} is a prime: {}".format(n, testprimality1(n, trial)))

# n, trial=int(sys.argv[1]), int(sys.argv[2])
# print("{} is a prime: {}".format(n, testprimality(n, trial)))

bits = 512
n = randint(1 << (bits - 1), 1 << bits)
while not testprimality1(n, trial):
    n = randint(1 << (bits - 1), 1 << bits)
print("{} is a prime: {}".format(n, testprimality1(n, trial)))
