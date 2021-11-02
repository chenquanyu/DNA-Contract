Cversion = '2.0.0'
from DNA.builtins import concat, substr, len
from DNA.interop.System.Runtime import Notify, CheckWitness
from DNA.interop.System.App import RegisterAppCall
from DNA.interop.System.ExecutionEngine import GetScriptContainer
from DNA.interop.System.Transaction import GetTransactionHash
from libs.require import *

OwnerKey = 'OwnerKey'
AssetPrefix = 'Asset-'
HistoryPrefix = 'History-'
StatusPrefix = 'Status-'
IssuerAddressPrefix = 'IssuerAddress-'
FinanceAddressPrefix = 'FinanceAddress-'
Name = 'Digital Asset'

# methods
getData = 'getData'
setData = 'setData'

issueAsset = 'issueAsset'
changeStatus = 'changeStatus'
pledgeAsset = 'pledgeAsset'
releaseAsset = 'releaseAsset'
getAsset = 'getAsset'

initOwner = 'initOwner'
changeOwner = 'changeOwner'
addIssuer = 'addIssuer'
removeIssuer = 'removeIssuer'
addFinance = 'addFinance'
removeFinance = 'removeFinance'

CallStorage = RegisterAppCall('8297129d680ea7d72b4484a6f82aa337ea5c26c5', 'operation', 'args')

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == IssueMethod:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return appendData(key, value)
    if operation == ChangeMethod:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return appendData(key, value)
    if operation == PledgeMethod:
        assert (len(args) == 1)
        key = args[0]
        return appendData(key, value)
    if operation == ReleaseMethod:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return appendData(key, value)
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

def initOwner(address):
    Notify([Name, "initOwner", address])
    return CallStorage(setData, [OwnerKey, address])

def changeOwner(address):
    owner = ToScriptHash(CallStorage(getData,[OwnerKey]))
    if CheckWitness(OWNER) == False:
        return False

    Notify([Name, "changeOwner", address])
    return CallStorage(setData, [OwnerKey, address])

def changeOwner(address):
    owner = ToScriptHash(CallStorage(getData,[OwnerKey]))
    if CheckWitness(OWNER) == False:
        return False

    Notify([Name, "changeOwner", address])
    return CallStorage(setData, [OwnerKey, address])

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

def pledge(key):
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