import itertools
"""
TO DO:
1) Split the plaintext in gold.plaintext.in into 32 bit sizes, if less than 32 pad the rest with 0s
*) Implement ECB
*) Implement CBC
*) Implement OFB
"""
#x^32 + x^15 + x^9 + x^7 + x^4 + x^3 + 1
irr = [ 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

def bin2int(B):
    n = 0
    for i in range(len(B)):
        if B[i] == 1:
            n += (2**(len(B)-i-1))
    return n

def xor(v1,v2):
    result = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        result.append(b)
    return result

def multiplication(A,B,irr):
    result = [ ]
    for i in range(len(A)):
        result.append(0)
    
    for i in range(len(A)):
        if B[i] == 1:
            shift = A
            for s in range(i):
                do_we_have_overflow = (shift[-1] == 1)
                shift = [0] + shift[:-1]
                if do_we_have_overflow:
                    shift = xor(shift, irr)
            result = xor(result,shift)
    return result

def gold(P):
    return multiplication( P, multiplication(P, P, irr), irr)

def encrypt(P,K):
    assert len(P) == 32
    assert len(K) == 32
    return xor(gold(P),K)

# Making 32-bit K that alternates 0s and 1s
key = [0]
for i in range(1, 32):
    if key[i - 1] == 0:
        key.append(1)
    else:
        key.append(0)

#ECB - Electronic codebook mode

#CBC - Cipherblock chaining mode

#OFB - Output feedback mode

#print(encrypt([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]))

# Read the file and outputs in binary
def plaintext_reader():
    with open("gold_plaintext.in", mode='rb') as file:
        while (byte := file.read(4)):
            print(byte, len(byte))
        

plaintext_reader()



