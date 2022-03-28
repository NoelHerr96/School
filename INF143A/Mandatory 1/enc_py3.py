from pydoc import plain
import sys

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
    # Original: [0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1]
    return multiplication(x,k,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1])

def round(INPUT,K):
    L = INPUT[:32]
    R = INPUT[32:]
    NEWL = [] + R
    NEWR = [] + xor(L, round_function(R,K))
    return NEWL + NEWR


def encrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        INPUT_BLOCK = round(INPUT_BLOCK,KEY)
        KEY = KEY[-4:] + KEY[:-4]
    return INPUT_BLOCK[32:] + INPUT_BLOCK[:32]

def decrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        KEY = KEY[4:] + KEY[:4]
        INPUT_BLOCK = round(INPUT_BLOCK,KEY)
    return INPUT_BLOCK[:32] + INPUT_BLOCK[32:]


# converter code from: https://www.alpharithms.com/python-convert-hexadecimal-to-binary-111821/
# kan gjøre litt mer "elegant" med å gjøre det om til fuctions

# 32bit key 3ACDDEF2
key_hexvalue = "3ACDDEF2"
key_intvalue = int(key_hexvalue, 16)
key = str(bin(key_intvalue))[2:].zfill(32)

real_key = "10101010101010101011101110111011"
key_to_list = [int(x) for x in real_key]
print("Your key in list: ", key_to_list, len(key_to_list))

# P = 1F2A0E341F2A0E34
plaintext_hexvalue = "1F2A0E341F2A0E34"
plaintext_intvalue = int(plaintext_hexvalue, 16)
plaintext = str(bin(plaintext_intvalue))[2:].zfill(64)
real_plain = "0001001000110100010101100111100010011010101111001101111011110000"
pt_to_list = [int(x) for x in real_plain]

print("Your plaintext in list: ", pt_to_list, len(pt_to_list))

print("Encrypted: ", encrypt(pt_to_list, key_to_list))

print("-------------"*5)


# C = AAAAAAAAAAAAAAAA
# ciphertext_hexvalue = "AAAAAAAAAAAAAAAA"
# ciphertext_intvalue = int(ciphertext_hexvalue, 16)
# ciphertext = str(bin(ciphertext_intvalue))[2:].zfill(64)
# ct_to_list = [int(x) for x in ciphertext]
# print("Your ciphertext in list: ", ct_to_list, len(ct_to_list))

# print("Ciphertext: ", decrypt(ct_to_list, key_to_list))



# string_ints = [str(int) for int in encrypt(pt_to_list, key_to_list)]
# print(string_ints)
# decrypt_toString = "".join(string_ints)
# int_decrypting = [int(x) for x in decrypt_toString]
# print("Decrypted: ", decrypt(int_decrypting, key_to_list))






