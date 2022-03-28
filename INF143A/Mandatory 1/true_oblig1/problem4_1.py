import random
import blackbox as enc

# Problem 4.1
# Written by Noel Santillana Herrera

n = 16
arr = [None] * n

p = "10101010101010101010101010101010"
c = "11110100011101010101100111111110"

key_lists = []

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
    
    # Gathering up the list of bruteforced keys for different keys
    for i in key_lists:
        key = [int(x) for x in i]
        bruteforced = enc.encrypt(plain_to_list, key)
        # If it matches the ciphertex, print it out
        if bruteforced == cipher_to_list:
            print("The ciphertext is: ", bruteforced)
            return key
        
key_generator(n, arr, 0)
print("Looking for key...")
print("The key used to get the ciphertext is: ", key_tester(p, c))

# Key output: 
# [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1]