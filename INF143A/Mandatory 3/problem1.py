import block as blk
"""
TO DO:
1) Split the plaintext in gold.plaintext.in into 32 bit sizes, if less than 32 pad the rest with 0s
*) Implement ECB
*) Implement CBC
*) Implement OFB
"""

BLOCK_SIZE = 32

# Making 32-bit IV-block
# iv = [1]
# for i in range(1, 32):
#    if iv[i - 1] == 0:
#        iv.append(1)
#    else:
#        iv.append(0)


# Making 32-bit K that alternates 0s and 1s
key = [0]
for i in range(1, 32):
    if key[i - 1] == 0:
        key.append(1)
    else:
        key.append(0)

#print(f"key: {key}, Len: {len(key)}")

#ECB - Electronic codebook mode
def ECB_mode():
    text_blocks = []
    ECB = []
    # Read the file and outputs in binary
    with open("gold_plaintext.in", mode='r') as file:
        while (byte := file.read(4)):
            text_blocks.append(str(byte))
    
    # https://stackoverflow.com/questions/30712020/typeerror-encoding-or-errors-without-a-string-argument
    for items in text_blocks:
        binary_converted = ' '.join(format(ord(c), 'b') for c in items)
        ECB.append(binary_converted)
    print(ECB)


    # for blocks in text_blocks:
    #     print(blocks)
        # assert len(blocks) == 32
        # assert len(key) == 32
        # encrypt = blk.xor(blk.gold(key), blocks)
        # ECB.append(encrypt)

    return ECB
        



#CBC - Cipherblock chaining mode

#OFB - Output feedback mode

        
ECB_mode()
