
#cython: language_level=3
#distutils: language=c++
# embedded.pyx

# The following two lines are for test purposed only, please ignore them.
# tag: py3only

TEXT_TO_SAY = 'Hello from Python!'

cdef public int say_hello_from_python() except -1:
    print(TEXT_TO_SAY)
    return 0
