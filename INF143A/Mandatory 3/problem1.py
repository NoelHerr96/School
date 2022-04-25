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
        encrypt = blk.xor(blk.gold(key), blocks)
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
    temp = []
    CBC_encrypted = []

    n = 0

    for i, element in enumerate(input):
        #making ciphertext block nr 1
        if i == 0:
            iv_step = blk.xor(element, iv)
            first_block = blk.xor(blk.gold(iv_step), key)
            CBC_encrypted.append(first_block)
        #making ciphertext block nr. 2
        elif i == 1:
            second_xor = blk.xor(element, first_block)
            second_block = blk.xor(blk.gold(second_xor), key)
            temp = element
            CBC_encrypted.append(second_block)
        #making ciphertext block n+1

    for lists in CBC_encrypted:
        xor_step = blk.xor(lists, temp)
        next_block = blk.xor(blk.gold(xor_step), key)

        CBC_encrypted.append(next_block)
    return CBC_encrypted

print(CBC_mode(bitfile_reader()))

#OFB - Output feedback mode

# print(bitfile_reader())
    