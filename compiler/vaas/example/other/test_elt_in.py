Cversion = '2.0.0'
#!/usr/bin/env python3
from DNA.libont import elt_in
from DNA.builtins import print

def VaasAssert(expr):
    if not expr:
        raise Exception("AssertError")
def main():
    operation = 'add'
    inor = 888
    if elt_in(['add','sub','mul'], operation):
        inor = 1
        print("in ")
    else:
        inor = 0
        print("not in")

    VaasAssert(inor == 1 + 1)

