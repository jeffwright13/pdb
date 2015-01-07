# epdb1.py -- experiment with the Python debugger, pdb

import pdb

a = "aaa"
pdb.set_trace()
b = "bbb"
pdb.set_trace()
c = "ccc"
pdb.set_trace()
final = a + b + c
pdb.set_trace()
print final