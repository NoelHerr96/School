"""Feistel network"""


"""Expansion table"""
E = [32, 1, 2, 3, 4, 5,
4, 5, 6, 7, 8, 9,
8, 9, 10, 11, 12, 13,
12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21,
20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32, 1]


"""S box table and function from ex 1.2"""
S = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]


def s_box_function(bitstring, S_box):
    assert len(bitstring) == 6
    assert bitstring == str(bitstring)

    row = int(bitstring[0]+bitstring[-1], 2)
    col = int(bitstring[1]+bitstring[2]+bitstring[3]+bitstring[4], 2)
    #print(row, col, "\n")

    output = S_box[row][col]
    output = bin(output)[2:].zfill(4)
    return output


"""Permutation table"""
P = [16, 7, 20, 21, 29, 12, 28, 17,
1, 15, 23, 26, 5, 18, 31, 10,
2, 8, 24, 14, 32, 27, 3, 9,
19, 13, 30, 6, 22, 11, 4, 25]


"""XOR function"""
def XOR(bit1, bit2):
    assert len(bit1) == len(bit2)
    length = len(bit1)
    a = int(bit1, 2)
    b = int(bit2, 2)
    c = a ^ b
    result = bin(c)[2:].zfill(length)
    return result


"""Feistel function"""
def feistel(input_block, round_key):
    assert len(input_block) == 32
    assert len(round_key) == 48

    #Expansion
    expanded = ""
    for i in range(len(E)):
        expanded = expanded + input_block[E[i] - 1]
    #print(expanded, len(expanded))

    #XOR with round key
    xor_bitstring = XOR(expanded, round_key)
    #print(xor_bitstring, len(xor_bitstring))

    #S boxes
    chunks = [xor_bitstring[i:i + 6] for i in range(0, len(xor_bitstring), 6)]
    #print(chunks)

    s_box_out = ""
    for part in chunks:
        s_box_out = s_box_out + s_box_function(part, S)
    #print(s_box_out, len(s_box_out))

    #Permutation
    permuted = ""
    for i in range(len(P)):
        permuted = permuted + s_box_out[P[i] - 1]
    #print(permuted, len(permuted))

    feistel_result = permuted
    return feistel_result


"""One round of DES"""
def round_function(input_block, round_key):
    assert len(input_block) == 64
    assert len(round_key) == 48

    left = input_block[:32]
    right = input_block[32:]

    left_out = right
    right_out = XOR(feistel(right, round_key), left)

    return left_out + right_out



key = "0"*48
half_block = "0"*32
#print(half_block)
#print(key)

r = feistel(half_block, key)
#print(r, len(r))

block = "0"*64
a = round_function(block, key)
#print(a, len(a))
