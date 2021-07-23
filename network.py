#cython: language_level=3
#distutils: language=c++

import cython 

if cython.compiled:
    print("NOTIFY: Yep, I'm network compiled.") 
else:
    print("WARN: Just a lowly network interpreted script.")




def start_network( a, b ):
    print("start network ", a , b) 



start_network(1000, 555) 
