import block as blk

"""
Written by Noel Santillana Herrera.
Problem 2. Matyas-Meyer-Oseas
1) Can use a vector of all 1s for the first round key h_0
2) What is the output size of this hash function?
3) How many hashes would an attacker have to compute in order to find a pair of inputs of the same hash(what would the so-called birthday attack be) 
4) Hash the plaintext in gold plaintext.in using the resulting hash function.
"""

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

    chunks=[temp[i:i + 32] for i in range(0, len(temp), 32)]
    
    for x, element in enumerate(chunks):
        while len(element) < 32:
            element.append(0)
        bits.append(element)
    return bits


def matyas_meyer_oseas(input):

    test_key = [1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]
    first_rkey = [1] * 32
    matyasmo = []
    n = 0

    for blocks in input:
        if n == 0:
            first_encrypt = blk.encrypt(blocks, first_rkey)
            first_xor = blk.xor(first_encrypt, blocks)
            matyasmo.append(first_xor)
            n += 1
        
        else:
            encrypt_step = blk.encrypt(blocks, matyasmo[-1])
            xor_step = blk.xor(encrypt_step, blocks)
            matyasmo.append(xor_step)

    


    # for x, element in enumerate(matyasmo):
    #     print(x, element)


    return matyasmo

# matyas_meyer_oseas(bitfile_reader())