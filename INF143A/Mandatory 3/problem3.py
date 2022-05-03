import block as blk
import hashlib
import binascii

"""
Code written by Noel Santillana Herrera
SHA-256 hash function
Got code help from Jan Edvard Nødland
To get outputs, simply run the code in an editor. 
"""

IV = [1] * 256

K = [0, 1] * 128




def bitfile_reader(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
        sha = hashlib.sha256()
        sha.update(data)
        sha_data= sha.hexdigest()

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

    chunks=[temp[i:i + 256] for i in range(0, len(temp), 256)]
    
    for x, element in enumerate(chunks):
        while len(element) < 256:
            element.append(0)
        bits.append(element)
    return bits



def bin_to_ascii(Bin):
    result = ""
    for i in range(0,len(Bin), 8):
        blocks = Bin[i:i+8]
        to_str = ''.join(map(str, blocks))
        characters = chr(int(to_str, 2))
        result += characters
    return result

def string_to_binary(string):
    binary_list = []
    binary = format(int(string, 16), "032b")
    for i in range (len(binary)):
        binary_list.append(int(binary[i]))
    return binary_list


def sha_convert(char):
    sha = hashlib.sha256(char.encode()).hexdigest()
    return sha

def sha256(bytes):
    hash_list = []
    first_m = IV
    first_k = K

    n = 0
    for bits in bytes:
        sum = first_k + first_m
        first_ascii = bin_to_ascii(sum)
        ascii_to_hash = sha_convert(first_ascii)
        ascii_to_hash = string_to_binary(ascii_to_hash)
        output = blk.xor(ascii_to_hash, bits)
        first_m = bits
    
    return output





print(sha256(bitfile_reader("gold_plaintext.in")))
print("Length of hash: ")
print(len(sha256(bitfile_reader("gold_plaintext.in"))))