# Problem 2
# Learned from https://www.ecrypt.eu.org/stream/ciphers/trivium/trivium.pdf

def trivium(v1, v2):
    result = []
    for i in range(4 * 288 + N):
        if i >= 4 * 288:
            b = (v1[i] + v2[i]) % 2
            result.append(b)
        else:
            continue
    return result
    
N = 1000
key = (1, 0, 1, 0,...,1, 0)
k_iv = (0, 1,..., 0, 1)

print(len(key))

k = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
iv = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]



# K = (1, 0, 1, 0,..., 1, 0) 80 alternating ones and zeros
# IV = (0, 1, 0, 1,...0, 1) 80 alternating zeros and ones
# generate 1000 bits of keystream.

# AND
# 0 AND 0 = 0
# 1 AND 0 = 0
# 0 AND 1 = 0
# 1 AND 1 = 1
# AND is represented by the ampersand - 1 & 1 = 1

# XOR
# 0 XOR 0 = 0
# 1 XOR 0 = 1
# 0 XOR 1 = 1
# 1 XOR 1 = 0
# XOR is represented by the upwards caret - 1 ^ 1 = 1