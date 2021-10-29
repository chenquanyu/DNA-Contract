from DNA.interop.System.ExecutionEngine import GetCallingScriptHash, GetEntryScriptHash,GetExecutingScriptHash
from DNA.interop.System.Runtime import Notify
from DNA.interop.DNA.Runtime import GetCurrentBlockHash
from DNA.builtins import *

def Main():
    C = [1, 2, 3, 4, 5, 6]
    for x in range(0, len(C)):
        C.append(x)
    for i in range(0, 20):
        Notify(C[i])
    return
