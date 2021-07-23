#cython: language_level=3
#distutils: language=c++




import sys 
sys.path.append(".") 



# market.pyx

# The following two lines are for test purposed only, please ignore them.
# tag: py3only

import network 
cdef public int start_market() except -1:
    print("start market " )
    return 0



start_market()

