Cversion = '2.0.0'
from DNA.builtins import print, bytearray

def VaasAssert(expr):
    if not expr:
        raise Exception("AssertError")
def Main():

    a = 3

    b = 2

    m = 12

    if not a == b:   # this currently works
        print("a not equal to b!!!")
        m = 21

    #VaasAssert(m == 21 + 1)

    if a != b:

        print("numbers 2 and 3 are not equal")
        m = 82

    #VaasAssert(m == 82 + 1 + 1)

    j = 'hello'
    k = 'hello'

    if j != k:

        print("string j is not equal to string k")
        m = 1

    else:
        m = 2

        print("string j is equal to string k")
    #VaasAssert(m == 2 + 1)

    q = bytearray(b'\x10\x01\x80')
    q2 = bytearray(b'\x10\x10\x80')

    if q != q2:
        m = 3
        print("bytearrays m and m2 not equal")

    else:
        m = 4

        print("bytearrays m and m2 are equal")
    #VaasAssert(m == 3 + 1)

    return m
