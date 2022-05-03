import block as blk

"""
Code written by Noel Santillana Herrera
"""

# Making 32-bit IV-block that consists of alternating 1s and 0s
iv = [1]
for i in range(1, 32):
   if iv[i - 1] == 0:
       iv.append(1)
   else:
       iv.append(0)

nik_iv = [1] * 32

# Making 32-bit K that alternates 0s and 1s
key = [0]
for i in range(1, 32):
    if key[i - 1] == 0:
        key.append(1)
    else:
        key.append(0)

# Nikolay's key 
nik_key = [1]*32



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
        encrypt = blk.encrypt(key, blocks)
        ECB_encrypted.append(encrypt)

    for x, element in enumerate(ECB_encrypted):
        print(x, element)
        
    return ECB_encrypted

# ECB_mode(bitfile_reader(read_file("output.ecb")))

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
            iv_step = blk.xor(block1, nik_iv)
            # print(f'iv_step: {iv_step}')
            first_block = blk.encrypt(iv_step, nik_key)
            CBC_encrypted.append(first_block)
            n += 1
        
        else:
            xor_step = blk.xor(block1, CBC_encrypted[-1])
            # print(f'xor_step: {xor_step}')
            cipherblock = blk.encrypt(xor_step, nik_key)
            CBC_encrypted.append(cipherblock)

    for x, element in enumerate(CBC_encrypted):
        print(x, element)
    return CBC_encrypted



#OFB - Output feedback mode
"""
1) IV and Key is encrpyted to get K1
2) K1 is XOR'd with Plaintext block nr 1, you get Ciphertext 1 as an output
3) Use Key and K1 is encrypted to get K2
4) K2 is XOR'd with Plaintext block nr 2, you get Ciphertext 2 as an output
5) Repeat step 3 but number increases by 1 for everything
"""
def OFB_mode(input):
    OFB_cipher = []
    key_generated = []

    n = 0
    for message in input:
        if n == 0:
            first_key = blk.encrypt(nik_iv,nik_key)
            key_generated.append(first_key)
            first_cipher = blk.xor(message, key_generated[-1])
            OFB_cipher.append(first_cipher)
            n += 1
        else:
            key_step = blk.encrypt(key_generated[-1], nik_key)
            key_generated.append(key_step)
            cipherblock = blk.xor(message, key_step)
            OFB_cipher.append(cipherblock)

    for x, element in enumerate(OFB_cipher):
        print(f'OFB: {x} {element}')

    return OFB_cipher

OFB_mode(bitfile_reader("gold_plaintext.in"))

# print(bitfile_reader("output.ofb"))