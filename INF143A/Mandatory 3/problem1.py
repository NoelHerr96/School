from os import remove
import block as blk

"""
TO DO:
1) Split the plaintext in gold.plaintext.in into 32 bit sizes, if less than 32 pad the rest with 0s
*) Implement ECB
*) Implement CBC
*) Implement OFB
"""

# Making 32-bit IV-block that consists of alternating 1s and 0s
iv = [1]
for i in range(1, 32):
   if iv[i - 1] == 0:
       iv.append(1)
   else:
       iv.append(0)


# Making 32-bit K that alternates 0s and 1s
key = [0]
for i in range(1, 32):
    if key[i - 1] == 0:
        key.append(1)
    else:
        key.append(0)

# Nikolay's key 
nik_key = [1]*32



def bitfile_reader():
    text_blocks = []
    temp = []
    final = []
    # Read the file and outputs in binary
    with open("gold_plaintext.in", mode='r') as file:
        while (byte := file.read()):
            text_blocks.append(byte)
    
    
    for items in text_blocks:
        binary_converted = ' '.join(format(ord(c), 'b') for c in items)
        remove_spaces = (binary_converted.replace(" ", ""))
        for j in remove_spaces:
            temp.append(int(j))

    # Splitting the list into 32-bit length chunks
    chunks=[temp[i:i + 32] for i in range(0, len(temp), 32)]


    for x, element in enumerate(chunks):
        while len(element) < 32:
            element.append(0)
        final.append(element)
    return final


# ECB - Electronic codebook mode
def ECB_mode(input):
    ECB_encrypted = []
    for blocks in input:
        encrypt = blk.encrypt(key, blocks)
        ECB_encrypted.append(encrypt)
    return ECB_encrypted

        
#CBC - Cipherblock chaining mode
"""
Process:
1) Message 1 XOR with IV(initialisastion vector), encrypt the xor'd with key, you get Ciphertext 1
2) Use Ciphertext 1 and XOR with Message 2, encrypt the xor'd with the key, you get Ciphertext 2
3) Same procedure as step 2, but XOR Ciptertext 2 with Message 3, encrypt the xor'd with key, 
4) repeat
"""
def CBC_mode(input):
    CBC_encrypted = []
    
    n = 0
    for block1 in input:
        # Making ciphertext 1
        if n == 0:
            iv_step = blk.xor(block1, iv)
            # print(f'iv_step: {iv_step}')
            first_block = blk.encrypt(iv_step, key)
            CBC_encrypted.append(first_block)
            n += 1
        
        else:
            xor_step = blk.xor(block1, CBC_encrypted[-1])
            # print(f'xor_step: {xor_step}')
            cipherblock = blk.encrypt(xor_step, key)
            CBC_encrypted.append(cipherblock)

    # for x, element in enumerate(CBC_encrypted):
    #     print(x, element)
    return CBC_encrypted

# CBC_mode(bitfile_reader())

#OFB - Output feedback mode
"""
1) IV and Key is encrpyted to get K1
2) K1 is XOR'd with Plaintext block nr 1, you get Ciphertext 1 as an output
3) Use Key and K1 is encrypted to get K2
4) K2 is XOR'd with Plaintext block nr 2, you get Ciphertext 2 as an output
5) Repeat step 3 but number increases by 1 for everything
"""
def OFB_mode(input):
    OFB_encrypted = []
    key_generate = []

    first_key = blk.encrypt(iv, key)
    key_generate.append(first_key)

    for block1 in input:
        cipherblck = blk.xor(block1, key_generate[-1])
        OFB_encrypted.append(cipherblck)
    
    for x, element in enumerate(OFB_encrypted):
        print(f'OFB: {x} {element}')

        return OFB_encrypted

