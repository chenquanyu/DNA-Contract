from DNA.interop.System.ExecutionEngine import GetCallingScriptHash, GetEntryScriptHash,GetExecutingScriptHash
from DNA.interop.System.Runtime import Notify
from DNA.interop.DNA.Runtime import GetCurrentBlockHash
from DNA.builtins import *
def Main(op,args):
    if op == "Mul":
        Mul(args[0],args[1])
        return True
    if op == "Add":
        Add(args[0],args[1])
        return True
    if op == "Left":
        Left(args[0],args[1])
        return True
    return False

def Mul(a,b):
    #Integer-Overflow-Occurred
    c = a * b
    Notify(c)
    return c

def Add(a,b):
    #Integer-Overflow-Occurred
    c = a + b
    Notify(c)
    return c

def Left(a,b):
    #Integer-Overflow-Occurred
    c = a << b
    Notify(c)
    return c

