# https://pypi.org/project/pylfsr/

# https://www.omnicalculator.com/math/linear-feedback-shift-register

import numpy as np 
from pylfsr import LFSR

## Example 3 ## To visualize the process with 3-bit LFSR, with default counter_start_zero = True
state = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
fpoly = [4, 2, 1]
L  = LFSR(initstate=state,fpoly=fpoly)
print('count \t state \t\toutbit \t seq')
print('-'*50)
for _ in range(50):
    print(L.count,L.state,'',L.outbit,L.seq,sep='\t')
    L.next()
print('-'*50)
print('Output: ',L.seq)



