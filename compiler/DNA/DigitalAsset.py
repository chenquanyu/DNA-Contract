Cversion = '2.0.0'
from DNA.builtins import *
from DNA.interop.System.Runtime import Notify, Base58ToAddress, Serialize, Deserialize
from DNA.interop.System.App import RegisterAppCall
from DNA.interop.System.ExecutionEngine import GetScriptContainer
from DNA.interop.System.Transaction import GetTransactionHash
from DNA.lib.require import *
from compiler.DNA.interop.System.Runtime import CheckWitness

OwnerKey = 'OwnerKey'
AssetPrefix = 'Asset-'
HistoryPrefix = 'History-'
StatusPrefix = 'Status-'
IssuerAddressMap = 'IssuerAddressMap'
FinanceAddressMap = 'FinanceAddressMap'
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
    if operation == issueAsset:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return issueAsset(key, value)
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
    if getData(OwnerKey):
        Notify("Already initialized!")
        return False
    Notify([Name, initOwner, address])
    setData()
    return setData(OwnerKey, address)

def changeOwner(address):
    requireOwner()
    Notify([Name, changeOwner, address])
    return setData(OwnerKey, address)

def addIssuer(address):
    requireOwner()
    Notify([Name, addIssuer, address])
    addressMapInfo = getData(IssuerAddressMap)
    addressMap = Deserialize(addressMapInfo)
    addressMap[address] =True
    return setData(Serialize(addressMap))
    
def removeIssuer(address):
    requireOwner()
    Notify([Name, removeIssuer, address])
    addressMapInfo = getData(IssuerAddressMap)
    addressMap = Deserialize(addressMapInfo)
    addressMap.remove(address)
    return setData(Serialize(addressMap))

def addFinance(address):
    requireOwner()
    Notify([Name, "changeOwner", address])
    return CallStorage(setData, [OwnerKey, address])

def removeFinance(address):
    requireOwner()
    Notify([Name, "changeOwner", address])
    return CallStorage(setData, [OwnerKey, address])

def requireIssuer():
    addressMapInfo = getData(IssuerAddressMap)
    addressMap = Deserialize(addressMapInfo)
    keys = addressMap.keys()

    for key in keys:
        if CheckWitness(key):
            return True
    raise Exception("Address is not witness")

def requireFinance():
    addressMapInfo = getData(FinanceAddressMap)
    addressMap = Deserialize(addressMapInfo)
    keys = addressMap.keys()

    for key in keys:
        if CheckWitness(key):
            return True
    raise Exception("Address is not witness")

def requireOwner():
    owner = Base58ToAddress(CallStorage(getData,[OwnerKey]))
    RequireWitness(owner)

def getData(key):
    # Notify([Name, getData, key])
    return CallStorage(getData, [key])

def setData(key, val):
    # Notify([Name, setData, key])
    return CallStorage(setData, [key, val])


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