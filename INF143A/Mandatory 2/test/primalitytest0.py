#!/usr/bin/env python
from random import *


def gcd(a, b):
    if a < 0 or b < 0:
        sys.exit("\n Integers a, b cannot be negative!\n")
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    while b > 0:
        return gcd(b, a % b)


def testprimality0(n):
    smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                   41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n < 100 and n in smallprimes:
        return True
    for prime in smallprimes:
        if n % prime == 0:
            return False
    for a in range(1, n):
        if gcd(a, n) > 1:
            return False
    return True


bits = 22

n = randint(1 << (bits - 1), 1 << bits)

# while not testprimality0(n):
#     n = randint(1 << (bits - 1), 1 << bits)
#     print("{} is a prime: {}".format(n, testprimality0(n)))

for n in range(2, 100):
    x = []
    for i in range(1, n):
        if i**2 % n == 1:
            x.append(i)
    if not testprimality0(n):
        print("{}, solutions = {}".format(n, x))
