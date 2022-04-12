import itertools

#XOR of binary vectors represented as strings
def xor(v1 , v2):
    assert len(v1) == len (v2)
    r = ''
    for i in range(len(v1) ):
        newsymbol = '0' if v1[i] == v2 [i] else '1'
        r = r + newsymbol
        return r

#F is given as an associative array of binary strings, e.g.
#F['000000'] = '010101' , etc.;n is the dimension
def differential_uniformity(F,n) :
    MAX = 0
    for a in itertools.product('01' , repeat=n) :
        #skip zero derivative direction
        if''.join(a) == '0'*n :
            continue
        #create a dictionary to count the number of times
        #each output difference appears
        hits = dict()
        for b in itertools.product('01' , repeat=n) :
            hits [''.join ( b ) ] = 0
        for x1 in itertools.product('01' , repeat=n) :
            x2 = xor(''.join(x1),''.join(a))
            y1 = F[''.join(x1)]
            y2 = F[''.join(x2)]
            hits[xor(y1 , y2 )] += 1
            #find the maximum number of hits
            localmax = 0
            for b in itertools.product('01', repeat=n) :
                if hits[''.join(b)] > localmax :
                    localmax = hits [''.join(b)]  
                #update the maximum if necessary
                if localmax > MAX:
                    MAX = localmax
    return MAX

print(differential_uniformity(000000, 6))