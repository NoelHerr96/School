import block as blk
import random

"""
Code written by Noel Santillana Herrera
SHA-256 hash function
1) Write a program that accepts a SHA-256 hash function to create encryption algorithm with the same approach as the one described in the text
2) 256-bit initialisation vector and a secret key of arbritrary length 
    * IV = 1, 1, 1,.. 1
    * K = 0, 1, 0, 1..0, 1
"""

IV = [1] * 256

K = [0]
for i in range (1, 64):
    if K [i-1] == 0:
        K.append(1)
    else:
        K.append(0)


def read_file(input_file):
    f = open(input_file, "rb")
    data = f.read()
    f.close()

    return data

def bitfile_reader(B):
    temp = []
    bits = []
    for i in range(len(B)):
        current_byte = B[i]
        mask = 128
        for j in range(8):
            if (current_byte >= mask):
                temp.append(1)
                current_byte -= mask
            else:
                temp.append(0)
            mask = mask // 2

    chunks=[temp[i:i + 64] for i in range(0, len(temp), 64)]
    
    for element in chunks:
        while len(element) < 64:
            element.append(0)
        bits.append(element)


    return bits


bitfile_reader(read_file("gold_plaintext.in"))

IV = [1] * 256

K = [0]
for i in range (1, 32):
    if K [i-1] == 0:
        K.append(1)
    else:
        K.append(0)


def hashing(input):
    hash = []
    first_m = IV

    n = 0
    for blocks in input:
        for i in blocks:
            if n == 0:
                first_m.append(i)
                while len(first_m) < len(IV):
                    first_m.append(0)
                print(first_m, len(first_m))
                n += 1



    return hash


hashing(bitfile_reader(read_file("gold_plaintext.in")))