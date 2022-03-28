state = 1 << 15 | 1
while True:
    print( state & 1, end='')
    newbit = (state ^ (state >> 3) ^ (state >> 12) ^ (state >> 14) ^ (state >> 15)) & 1
    state = (state >> 1) | (newbit << 15)
