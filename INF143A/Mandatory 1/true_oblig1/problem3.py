from pydoc import plain

# Problem 3
# Feistel cipher modified by Noel Santillana Herrera
# Because of how problem 3 is almost like problem 4, 
# I have taken the code from the blackbox and modified it to solve for this problem

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

def round_function(x,k):
    # round function F(x) = f(x, k) = (x^2)k + xk^2
    # x is right half
    # k is round key
    irr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    left_half = multiplication(multiplication(x,x,irr), k, irr)
    right_half = multiplication(x, multiplication(k, k, irr), irr)
    result = xor(left_half, right_half)
    return result

def round_enc(INPUT,K):
    L = INPUT[:32]
    R = INPUT[32:]
    NEWL = [] + R
    NEWR = [] + xor(L, round_function(R,K))
    return NEWL + NEWR

def encrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        INPUT_BLOCK = round_enc(INPUT_BLOCK,KEY)
        KEY = KEY[-4:] + KEY[:-4]
    return INPUT_BLOCK[:32] + INPUT_BLOCK[32:]

def round_dec(INPUT, K):
    L = INPUT[:32]
    R = INPUT[32:]
    NEWR = [] + L
    NEWL = [] + xor(R, round_function(L,K))
    return NEWL + NEWR


def decrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        KEY = KEY[4:] + KEY[:4]
        INPUT_BLOCK = round_dec(INPUT_BLOCK,KEY)
    return INPUT_BLOCK[:32] + INPUT_BLOCK[32:]


# 32bit key 3ACDDEF2
real_key = "10101010101010101011101110111011"
key_to_list = [int(x) for x in real_key]

# P = 1F2A0E341F2A0E34
real_plain = "0001001000110100010101100111100010011010101111001101111011110000"
pt_to_list = [int(x) for x in real_plain]


print("-------------"*5)
print("Encrypted: ", encrypt(pt_to_list, key_to_list))
# Output:
# [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 
# 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]
print("-------------"*5)


# C = AAAAAAAAAAAAAAAA.
real_cipher = "0011101000111101111011111111011110101011101110101100100011011011"
int_decrypting = [int(x) for x in real_cipher]
print("Decrypted: ", decrypt(int_decrypting, key_to_list))
# Output:
#[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 
#1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]