Cversion = '2.0.0'
from DNA.libont import bytearray_reverse, hexstring2bytes
from DNA.interop.System.App import RegisterAppCall, DynamicAppCall
from DNA.interop.System.Runtime import Notify
from DNA.interop.System.Storage import GetContext, Get, Put, Delete

Name = 'Router'

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == 'setContract':
        assert (len(args) == 2)
        name = args[0]
        address = args[1]
        return setContract(name, address)
    if operation == 'callContract':
        assert (len(args) == 3)
        name = args[0]
        operation = args[1]
        params = args[2]
        return callContract(name, operation, params)
    return False

def name():
    return Name

def setContract(name, address):
    assert(len(address) == 40)
    reversedContractAddress = bytearray_reverse(hexstring2bytes(address))
    Put(GetContext(), name, reversedContractAddress)
    Notify([Name, "setContract", name, address])
    return True

def callContract(name, operation, params):
    reversedContractAddress = Get(GetContext(), name)
    res = DynamicAppCall(reversedContractAddress, operation, params)
    Notify([Name, "callContract", name, operation])
    return res