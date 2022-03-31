#!/usr/bin/env python
from random import *
from BitVector import *


def testprimality3(p):  # Miller Robin test
    if p == 1:
        return 0
    probes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if p in probes:
        return 1
    if any([p % a == 0 for a in probes]):
        return 0
    # need to represent p-1 as  q * 2^k
    k, q = 0, p - 1
    while not q & 1:
        q >>= 1
        k += 1
    for a in probes:
        a_raised_to_q = pow(a, q, p)
        if a_raised_to_q == 1:
            continue
        if (a_raised_to_q == p - 1) and (k > 0):
            continue
        a_raised_to_jq = a_raised_to_q
        primeflag = 0
        for j in range(k - 1):
            a_raised_to_jq = pow(a_raised_to_jq, 2, p)
            if a_raised_to_jq == p - 1:
                primeflag = 1
                break  # (A20)
        if not primeflag:
            return 0
    probability_of_prime = 1 - 1.0 / (4 ** len(probes))
    return probability_of_prime


def main():
    n_bv = BitVector(intVal=0)
    bits = int(input("Provide the number of bits of the requested prime: "))
    n = int(n_bv.gen_random_bits(bits))
    while not testprimality3(n):
        n = int(n_bv.gen_random_bits(bits))
    print("{} is a prime with probaility {}\n".format(n, testprimality3(n)))


if __name__ == '__main__':
    main()
