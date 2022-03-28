# Problem 2

"""Written by Noel Santillana Herrera"""

def Trivium(iv_inp, key_inp, third_inp):
    
    #BLOCK_1 IV of 93-degree
    BLOCK_1 = iv_inp
    
    #BLOCK_2 KEY of 84-degree
    BLOCK_2 = key_inp

    #BLOCK_3 111-degree LFSR
    BLOCK_3 = third_inp  
      
    # KEYSTREAM
    KEYSTREAM = []
    
    N = 1000
    for i in range(4*288 + N):
            
        # RIGHT SIDE OUT: (91 AND 92) XOR W/ 93 + 66 
        BLOCK_1_out = (BLOCK_1[90] & BLOCK_1[91]) ^ BLOCK_1[92] ^ BLOCK_1[65]

        # RIGHT SIDE OUT: (82 AND 83) XOR W/ 84 + 69 
        BLOCK_2_out = (BLOCK_2[81] & BLOCK_2[82]) ^ BLOCK_2[83] ^ BLOCK_2[68]

        # RIGHT SIDE OUT: (109 AND 110) XOR W/ 111 + 66
        BLOCK_3_out = (BLOCK_3[108] & BLOCK_3[109]) ^ BLOCK_3[110] ^ BLOCK_3[65]


        #Going inside BLOCK 1, 2, 3
        # BLOCK 1, LEFT SIDE IN: XOR from output of BLOCK3 with 69th-bit
        BLOCK_1_in = BLOCK_3_out ^ BLOCK_1[68]
        # BLOCK 2, LEFT SIDE IN: XOR from output of BLOCK 1 with 78th-bit
        BLOCK_2_in = BLOCK_1_out ^ BLOCK_2[77]
        # BLOCK 3, LEFT SIDE IN: XOR from output of BLOCK 2 with 87th-bit
        BLOCK_3_in = BLOCK_2_out ^ BLOCK_3[86]

        # remove most right bit
        BLOCK_1.pop()
        BLOCK_2.pop()
        BLOCK_3.pop()
        
        # inserting the ingoing XOR'd bit
        BLOCK_1.insert(0, BLOCK_1_in)
        BLOCK_2.insert(0, BLOCK_2_in)
        BLOCK_3.insert(0, BLOCK_3_in)
              
        # XOR from output of BLOCK 1, 2 & 3
        if i >= 1152:
            GEN_KEYSTREAM = BLOCK_1_out ^ BLOCK_2_out ^ BLOCK_3_out
            KEYSTREAM.append(GEN_KEYSTREAM)
    print("Your keystream of 1000-bits is: ")
    return KEYSTREAM


# Making 93-bit IV-block
iv = [0]
for i in range(1, 80):
    if iv[i - 1] == 0:
        iv.append(1)
    else:
        iv.append(0)
while len(iv) < 93:
    iv.append(0)


# Making 84-bit key-block
key = [1]
for i in range(1, 80):
    if key[i - 1] == 0:
        key.append(1)
    else:
        key.append(0)  
while len(key) < 84:
    key.append(0)


# Making third-block
third_block = []
for i in range (0, 108):
    third_block.append(0)
while len(third_block) < 111:
    third_block.append(1)


print(Trivium(iv, key, third_block))
# print out of first 50 keystream
# [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 
# 0, 0, 1, 1, 0, 1, 0, 1, 0, 1]