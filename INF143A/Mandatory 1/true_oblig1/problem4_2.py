import random
import blackbox as enc

# Problem 4.2
# Written by Noel Santillana Herrera

n = 16
arr = [None] * n

p = "10101010101010101010101010101010"
c = "11000110100010110110000001101110"

key_lists = []

# A helper method to turn the keys into string
def to_string(arr):
    string = ""
    for char in arr:
        string += str(char)
    return string

def key_generator(n, arr, i):
    if i == n:
        key_lists.append(to_string(arr))
        return
    
    arr[i] = 0
    key_generator(n, arr, i + 1)
    
    arr[i] = 1
    key_generator(n, arr, i + 1)


def key_tester(plain, cipher):
    # Turn plain- and ciphertext to a list
    plain_to_list = [int(x) for x in plain]
    cipher_to_list = [int(x) for x in cipher]
    encrypted = []
    pairing = []
    
    # Gathering up the list of bruteforced keys with different keys
    for i in key_lists:
        key = [int(x) for x in i]
        bruteforced = enc.encrypt(plain_to_list, key)
        encrypted.append(bruteforced)
    
    # Gathering up the list of decrypted keys with different keys
    for k2 in key_lists:
        k2 = [int(x) for x in k2]
        decrypted = enc.decrypt(cipher_to_list, k2)
        for i in range(len(encrypted)):
            
            # Matching up if the encrypted[i] is similar to the decrypted "text"
            if encrypted[i] == decrypted:
                k1 = key_lists[i]
                print(f"key 1 {k1} + key 2{k2}")
                pairing.append((k1, k2))

    return pairing
                
                      
        
key_generator(n, arr, 0)
print("Running... From my Noel's computer this took around 9mins")
print("The keys are: ", key_tester(p, c))

#Output
# key 1 0100011110010111 + key 2[0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
# key 1 1011111010001010 + key 2[1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
# key 1 0000000000000111 + key 2[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
