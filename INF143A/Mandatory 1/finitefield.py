def xor(v1,v2):
    result = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        result.append(b)
    return result

def multiplication(A,B,irr):
    result = [ ]
    for i in range(len(A)):
        result.append(0)
        
    for i in range(len(A)):
        if B[i] == 1:
          shift = A
        for s in range(i):
            do_we_have_overflow = (shift[-1] == 1)
            shift = [0] + shift[:-1]
            if do_we_have_overflow:
                shift = xor(shift, irr)
                result = xor(result,shift)
    return result

#print multiplication([1,1,0,0], [1,1,1,1], [1,1,0,0])
print (multiplication([1,1,0,0,0,1,0,1], [1,1,1,1,0,0,1,0], [ 1, 0, 1, 1, 1, 0,
0, 0 ]))