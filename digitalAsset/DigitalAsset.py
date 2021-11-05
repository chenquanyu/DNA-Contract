Cversion = '2.0.0'
from DNA.builtins import *
from DNA.interop.System.Runtime import Notify, Serialize, Deserialize, CheckWitness
from DNA.interop.System.App import RegisterAppCall
from DNA.lib.require import *
from DNA.interop.DNA.Runtime import Base58ToAddress

OwnerKey = 'OwnerKey'
AssetPrefix = 'Asset-' # AssetMap stores the current info of asset
HistoryPrefix = 'History-' # History list stores all the asset history, including current
IssuerAddressMap = 'IssuerAddressMap'
FinanceAddressMap = 'FinanceAddressMap'
Name = 'Digital Asset'
AssetInfo = 'AssetInfo'
FinanceInfo = 'FinanceInfo'

# methods
getData = 'getData'
setData = 'setData'

issueAsset = 'issueAsset'
changeStatus = 'changeStatus'
pledgeAsset = 'pledgeAsset'
releaseAsset = 'releaseAsset'
getAsset = 'getAsset'
getAssetHistory = 'getAssetHistory'

initOwner = 'initOwner'
changeOwner = 'changeOwner'
addIssuer = 'addIssuer'
removeIssuer = 'removeIssuer'
addFinance = 'addFinance'
removeFinance = 'removeFinance'

CallStorage = RegisterAppCall("f84d079e3e6eedccd0be29a01c902e03c8d325d2", 'operation', 'args')

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == issueAsset:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return issueAssetF(key, value)
    if operation == changeStatus:
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return changeStatusF(key, value)
    if operation == pledgeAsset:
        assert (len(args) == 3)
        key = args[0]
        value1 = args[1]
        value2 = args[2]
        return pledgeAssetF(key, value1, value2)
    if operation == releaseAsset:
        assert (len(args) == 3)
        key = args[0]
        value1 = args[1]
        value2 = args[2]
        return releaseAssetF(key, value1, value2)
    if operation == getAsset:
        assert (len(args) == 1)
        key = args[0]
        return getAssetF(key)
    if operation == getAssetHistory:
        assert (len(args) == 1)
        key = args[0]
        return getAssetHistoryF(key)

    if operation == initOwner:
        assert (len(args) == 1)
        key = args[0]
        return initOwnerF(key)
    if operation == changeOwner:
        assert (len(args) == 1)
        key = args[0]
        return changeOwnerF(key)
    if operation == addIssuer:
        assert (len(args) == 1)
        key = args[0]
        return addIssuerF(key)
    if operation == removeIssuer:
        assert (len(args) == 1)
        key = args[0]
        return removeIssuerF(key)
    if operation == addFinance:
        assert (len(args) == 1)
        key = args[0]
        return addFinanceF(key)
    if operation == removeFinance:
        assert (len(args) == 1)
        key = args[0]
        return removeFinanceF(key)

def name():
    return Name

def getAssetKey(assetId):
    return concat(AssetPrefix, assetId)

def getHistoryKey(assetId):
    return concat(HistoryPrefix, assetId)

def issueAssetF(assetId, assetInfo):
    requireIssuer()
    Notify([Name, issueAsset, assetId])
    map = {
        "AssetInfo" : assetInfo,
        "FinanceInfo" : ""
    }
    setDataF(getAssetKey(assetId), Serialize(map))
    # add history
    addHistory(assetId, map)
    return True

def changeStatusF(assetId, assetInfo):
    requireIssuer()
    Notify([Name, changeStatus, assetId])
    oldMap = Deserialize(getDataF(getAssetKey(assetId)))
    # change asset info
    newMap = {
        AssetInfo : assetInfo,
        FinanceInfo : oldMap[FinanceInfo]
    }
    setDataF(getAssetKey(assetId), Serialize(newMap))
    # add history
    addHistory(assetId, newMap)
    return True

def pledgeAssetF(assetId, assetInfo, financeInfo):
    requireFinance()
    Notify([Name, pledgeAsset, assetId])
    # change asset and finance info
    newMap = {
        AssetInfo : assetInfo,
        FinanceInfo : financeInfo
    }
    setDataF(getAssetKey(assetId), Serialize(newMap))
    # add history
    addHistory(assetId, newMap)
    return True

def releaseAssetF(assetId, assetInfo, financeInfo):
    requireFinance()
    Notify([Name, releaseAsset, assetId])
    # change asset and finance info
    newMap = {
        AssetInfo : assetInfo,
        FinanceInfo : financeInfo
    }
    setDataF(getAssetKey(assetId), Serialize(newMap))
    # add history
    addHistory(assetId, newMap)
    return True

def getAssetF(assetId):
    Notify([Name, getAsset, assetId])
    assetByte = getDataF(getAssetKey(assetId))
    if assetByte == None:
        return ""
    return getMapJson(assetByte)
    
def getAssetHistoryF(assetId):
    Notify([Name, getAssetHistory, assetId])
    hisByte = getDataF(getHistoryKey(assetId))
    if hisByte == None:
        return "[]"
    return getListJson(hisByte)

def initOwnerF(address):
    if getDataF(OwnerKey):
        raise Exception("Already initialized!")
    Notify([Name, initOwner, address])
    return setDataF(OwnerKey, address)

def changeOwnerF(address):
    requireOwner()
    Notify([Name, changeOwner, address])
    return setDataF(OwnerKey, address)

def addIssuerF(address):
    requireOwner()
    Notify([Name, addIssuer, address])
    return addMap(IssuerAddressMap, address, True) 
    
def removeIssuerF(address):
    requireOwner()
    Notify([Name, removeIssuer, address])
    return removeMap(IssuerAddressMap, address)

def addFinanceF(address):
    requireOwner()
    Notify([Name, addFinance, address])
    return addMap(FinanceAddressMap, address, True)

def removeFinanceF(address):
    requireOwner()
    Notify([Name, addFinance, address])
    return removeMap(FinanceAddressMap, address)

# util methods

def requireIssuer():
    addressMapInfo = getDataF(IssuerAddressMap)
    addressMap = Deserialize(addressMapInfo)
    keys = addressMap.keys()

    for key in keys:
        if CheckWitness(Base58ToAddress(key)):
            return True
    raise Exception("Address is not witness")

def requireFinance():
    addressMapInfo = getDataF(FinanceAddressMap)
    addressMap = Deserialize(addressMapInfo)
    keys = addressMap.keys()

    for key in keys:
        if CheckWitness(Base58ToAddress(key)):
            return True
    raise Exception("Address is not witness")

def requireOwner():
    owner = Base58ToAddress(getDataF(OwnerKey))
    RequireWitness(owner)

def addMap(mapKey, key, val):
    mapInfo = getDataF(mapKey)
    if mapInfo == None:
        map = {}
    else:
        map = Deserialize(mapInfo)
    map[key] = val
    return setDataF(mapKey, Serialize(map))

def removeMap(mapKey, key):
    mapInfo = getDataF(mapKey)
    map = Deserialize(mapInfo)
    map.remove(key)
    return setDataF(mapKey, Serialize(map))

def addHistory(assetId, oldMap):
    hisKey = getHistoryKey(assetId)
    hisInfo = getDataF(hisKey)
    if hisInfo == None:
        history = []
    else:
        history = Deserialize(hisInfo)
    history.append(oldMap)
    setDataF(hisKey, Serialize(history))

def getDataF(key):
    return CallStorage(getData, [key])

def setDataF(key, val):
    return CallStorage(setData, [key, val])

def getListJson(listByte):
    list = Deserialize(listByte)
    res = "["
    for item in list:
        res = concat(concat(res, getMapJson(Serialize(item))), ",")
    if substr(res, len(res)-1, 1) == "," :  
        res = substr(res, 0, len(res) - 1)
    res = concat(res, "]")
    return res

def getMapJson(mapByte):
    map = Deserialize(mapByte)
    res = "{"
    for key in map.keys():
        res = concat(concat(concat(res,'"'), key), '":"')
        res = concat(concat(res, map[key]), '",')
    if substr(res, len(res)-1, 1) == ",":   
        res = substr(res, 0, len(res) - 1)
    res = concat(res, "}")
    return res
