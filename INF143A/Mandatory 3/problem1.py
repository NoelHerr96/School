import block as blk

"""
TO DO:
1) Split the plaintext in gold.plaintext.in into 32 bit sizes, if less than 32 pad the rest with 0s
*) Implement ECB
*) Implement CBC
*) Implement OFB
"""

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

def bitfile_reader():
    text_blocks = []
    placeholder = []
    # Read the file and outputs in binary
    with open("gold_plaintext.in", mode='r') as file:
        while (byte := file.read()):
            text_blocks.append(byte)
    
    # https://stackoverflow.com/questions/30712020/typeerror-encoding-or-errors-without-a-string-argument
    for items in text_blocks:
        binary_converted = ' '.join(format(ord(c), 'b') for c in items)
        placeholder = (binary_converted.replace(" ", ""))
        
    return placeholder



#ECB - Electronic codebook mode
# def ECB_mode(input):
#     # binary_lists = [input[x:x+32] for x in range(0, len(input), 32)]
#     ECB = []

#     # Adding commas
#     for i in input:
#         temp = []
#         for j in i:
#             j.split(',')
#             ECB.append(j)

#     # Splitting the list into 32 length chunks
#     output=[ECB[i:i + 32] for i in range(0, len(ECB), 32)]
    

    # ECB_solved = []
    # for blocks in output:
    #     encrypt = blk.xor(blk.gold(key), blocks)
    #     ECB_solved.append(encrypt)


        


#CBC - Cipherblock chaining mode

#OFB - Output feedback mode

print(bitfile_reader())
    