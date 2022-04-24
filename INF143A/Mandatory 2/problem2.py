"""
Miller-Rabin implementation

To verify if the very long integer is prime: I used https://bigprimes.org/primality-test
To verify if the large prime returned back is the number of bitsize I used https://www.mobilefish.com/services/big_number/big_number.php .
"""
import random

# Returned True means it is prime
# Returned False means it is not prime
def miller_rabin_test(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n-1
    
    while d % 2 == 0:
        r += 1
        d //=2
        
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        
        if x == 1 or x == n-1:
            continue
        for _ in range (r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def binary_toInt(B):
    n = 0
    pow_2 = 1
    #Everytime there's a 1 in there, we add a power of 2
    #Basically turn our list 0s and 1s into integer for the miller-rabin
    for i in reversed(range(len(B))):
        n += pow_2 * B[i]
        pow_2 *= 2
    return n

# Get a value with a specified number of bits
def int_value(bits):
    B=[0] * bits
    B[0] = 1
    B[-1] = 1 
    for i in range(1, bits - 1):
        B[i] = random.randint(0, 1)
    return binary_toInt(B)

#Generate our prime with specified number of bits
def generate_prime(bits):
    while True:
        n = int_value(bits)
        if miller_rabin_test(n, 40):
            print(f"Your prime number of {bits} bits is: {n}")
            break


generate_prime(500)
generate_prime(671)
generate_prime(1024)

        