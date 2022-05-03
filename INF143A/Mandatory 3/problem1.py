import block as blk

"""
Code written by Noel Santillana Herrera
To get outputs, scroll to the bottom and remove their prints, and then simply run the code in an editor. 
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

# Nikolay's key and IV for testing
nik_key = [1]*32
nik_iv = [1] * 32


def bitfile_reader(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    temp = []
    bits = []
    for i in range(len(data)):
        current_byte = data[i]
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



# ECB - Electronic codebook mode
def ECB_mode(input):
    ECB_encrypted = []
    for blocks in input:
        encrypt = blk.encrypt(blocks, key)
        ECB_encrypted.append(encrypt)

    for x, element in enumerate(ECB_encrypted):
        print(f"{x}. Output for ECB {element}")
        
    return ECB_encrypted


# CBC - Cipherblock chaining mode
def CBC_mode(bytes):
    CBC_encrypted = []
    
    n = 0
    for message in bytes:
        # Making ciphertext 1
        if n == 0:
            iv_step = blk.xor(message, iv)
            first_block = blk.encrypt(iv_step, key)
            CBC_encrypted.append(first_block)
            n += 1
        
        else:
            xor_step = blk.xor(message, CBC_encrypted[-1])
            cipherblock = blk.encrypt(xor_step, key)
            CBC_encrypted.append(cipherblock)
    
    for x, element in enumerate(CBC_encrypted):
        print(f"{x}. Output for CBC {element}")


    return CBC_encrypted


# OFB - Output feedback mode
def OFB_mode(input):
    OFB_cipher = []
    key_generated = []

    n = 0
    for message in input:
        if n == 0:
            first_key = blk.encrypt(iv, key)
            key_generated.append(first_key)
            first_cipherblock = blk.xor(message, key_generated[-1])
            OFB_cipher.append(first_cipherblock)
            n += 1
        else:
            key_step = blk.encrypt(key_generated[-1], key)
            key_generated.append(key_step)
            cipherblock = blk.xor(message, key_step)
            OFB_cipher.append(cipherblock)


    for x, element in enumerate(OFB_cipher):
            print(f"{x}. Output for OFB {element}")

    return OFB_cipher


#ECB_mode(bitfile_reader("gold_plaintext.in"))
#CBC_mode(bitfile_reader("gold_plaintext.in"))
#OFB_mode(bitfile_reader("gold_plaintext.in"))
