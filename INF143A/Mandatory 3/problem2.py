import block as blk

"""
Code written by Noel Santillana Herrera.
Problem 2. Matyas-Meyer-Oseas
To get outputs, simply run the code in an editor. 
"""

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


def matyas_meyer_oseas(bits):

    IV = [1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]
    first_iv = [1] * 32
    matyasmo = []

    n = 0
    for message in bits:
        if n == 0:
            first_step = blk.encrypt(message, first_iv)
            first_xor = blk.xor(first_step, message)
            matyasmo.append(first_xor)
            n += 1
        else:
            encryption = blk.encrypt(message, matyasmo[-1])
            hash_generate = blk.xor(encryption, message)
            matyasmo.append(hash_generate)


    

        return matyasmo


print(matyas_meyer_oseas(bitfile_reader("gold_plaintext.in")))

print("The output size of this hash function is 32-bits. The attacker would have to compute 2^32(~4,3 * 10^9) in order to find a pair of inputs with the same hash")
print("Source for birthday attack taken from table from: ")