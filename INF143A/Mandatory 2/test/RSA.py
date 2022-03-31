#!/usr/bin/env python
from random import *
from BitVector import *
from MillerRobin import *


def xgcd(a, b):
    if a < 0 or b < 0:
        sys.exit("\n Integers a, b cannot be negative!\n")
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return xgcd(b, a)
    r = [a, b]
    u = [1, 0]
    v = [0, 1]
    while r[-2] % r[-1] != 0:
        q = r[-2] // r[-1]
        r.append(r[-2] - q * r[-1])
        u.append(u[-2] - q * u[-1])
        v.append(v[-2] - q * v[-1])
    # print(r)
    # print(u)
    # print(v)
    return r[-1], v[-1], u[-1]


def generateRSAKey(len):
    bv = BitVector(intVal=0)
    p = int(bv.gen_random_bits(len))
    while test_integer_for_prime(p) <= 0.9999:
        p = int(bv.gen_random_bits(len))
    q = int(bv.gen_random_bits(len))
    while test_integer_for_prime(q) <= 0.9999:
        q = int(bv.gen_random_bits(len))
    n = p * q
    e = 2**4 + 1
    phi_n = (p - 1) * (q - 1)
    t, v, u = xgcd(e, phi_n)
    if t == 1:
        d = (phi_n + v) % phi_n
        # print(e * d % phi_n == 1)
        return [n, e], [p, q, d]


def main():
    keylen = int(input("Length of the prime p or q: "))
    pubkey, prikey = generateRSAKey(keylen)
    ptxt = int(input("Integer of plaintxt: "))
    n = pubkey[0]
    e = pubkey[1]
    d = prikey[2]
    if n <= ptxt:
        sys.exit("The input plaintxt exceeds the limit\n")
    print("RSA PubKeys: {}\nRSA Private Keys: {}".format(pubkey, prikey))
    ctxt = pow(ptxt, e, n)
    print("\nInteger of Ciphetext: ", ctxt)
    print("Decryption Test: ", pow(ctxt, d, n) == ptxt)


if __name__ == '__main__':
    main()
