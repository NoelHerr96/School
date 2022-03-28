"""S box"""


#print("hello")

S = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

#print(S[0][0])


"""Gives the 4-bit output of the s_box from a 6-bit input, Ex 1.2"""
def s_box_function(bitstring, S_box):
    assert len(bitstring) == 6
    assert bitstring == str(bitstring)

    row = int(bitstring[0]+bitstring[-1], 2)
    col = int(bitstring[1]+bitstring[2]+bitstring[3]+bitstring[4], 2)
    #print(row, col, "\n")

    output = S_box[row][col]
    output = bin(output)[2:].zfill(4)
    return output

"""print(s_box_function("100010", S))
print(s_box_function("000000", S))
print(s_box_function("000001", S))
print(s_box_function("111111", S))
print(s_box_function("100000", S))
print(s_box_function("101010", S))
print(s_box_function("010101", S))"""


"""Counts the number of linear pairs of the s_box, Ex 1.3"""
def linear_counter(S_box):
    size = len(S_box)*len(S_box[0])
    count = 0
    pairs = 0

    for x in range(size):
        x_i = bin(x)[2:].zfill(6)
        for y in range(size):
            y_i = bin(y)[2:].zfill(6)
            #print(x, y)
            pairs += 1

            #S(x)
            s_x = s_box_function(x_i, S_box)
            #S(y)
            s_y = s_box_function(y_i, S_box)

            z = int(x_i, 2) ^ int(y_i, 2)
            z = bin(z)[2:].zfill(6)
            #S(x + y)
            s_z = s_box_function(z, S_box)

            if int(s_x, 2) ^ int(s_y, 2) == int(s_z, 2):
                count += 1

    ratio = (1.0*count) / pairs
    return count, pairs, ratio


print(linear_counter(S))
