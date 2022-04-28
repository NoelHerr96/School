import block as blk

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
for i in range (1, 256):
    if K [i-1] == 0:
        K.append(1)
    else:
        K.append(0)

