Cversion = '2.0.0'
from DNA.interop.System.Storage import GetContext, Get, Put, Delete
from DNA.interop.System.Runtime import Notify, CheckWitness
from DNA.interop.DNA.Runtime import Base58ToAddress

Name = 'Storage'

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == 'getData':
        assert (len(args) == 1)
        key = args[0]
        return getData(key)
    if operation == 'setData':
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return setData(key, value)
    if operation == 'deleteData':
        assert (len(args) == 1)
        key = args[0]
        return deleteData(key)
    return False

def name():
    return Name

def getData(key):
    sc = GetContext()
    Notify([Name, "getData", key])
    return Get(sc, key)

def setData(key, value):
    sc = GetContext()
    Put(sc, key, value)
    Notify([Name, "setData", key])
    return True

def deleteData(key):
    sc = GetContext()
    Delete(sc, key)
    Notify([Name, "deleteData", key])
    return True