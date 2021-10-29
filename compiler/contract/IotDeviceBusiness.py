Cversion = '2.0.0'
from DNA.builtins import concat, substr, len
from DNA.interop.System.Runtime import Notify
from DNA.interop.System.App import RegisterAppCall
from DNA.interop.System.ExecutionEngine import GetScriptContainer
from DNA.interop.System.Transaction import GetTransactionHash

HistoryPrefix = 'History-'
Name = 'Iot Device Business'

GetMethod = 'getData'
SetMethod = 'setData'
CallStorage = RegisterAppCall('57a2ca15e343c68589e7ea7c5f4229a315a35d43', 'operation', 'args')

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == 'getData':
        assert (len(args) == 1)
        key = args[0]
        return getData(key)
    if operation == 'appendData':
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return appendData(key, value)

def name():
    return Name

def getData(key):
    Notify([Name, "getData", key])
    return CallStorage(GetMethod, [key])

def appendData(key, value):
    historyKey = concat(HistoryPrefix, key)
    oldValue = CallStorage(GetMethod, [key])
    oldHistory = CallStorage(GetMethod, [historyKey])
    Notify([Name, "appendData", key])
    if oldHistory == None:
        newHistory = concat(concat('[', value), ']')
        return CallStorage(SetMethod, [historyKey, newHistory]) and CallStorage(SetMethod, [key, value])
    else:
        hisContent = substr(oldHistory, 1, len(oldHistory)-2)
        newHistory = concat(concat(concat(concat('[',hisContent),','), value),']')
        return CallStorage(SetMethod, [historyKey, newHistory]) and CallStorage(SetMethod, [key, value])