Cversion = '2.0.0'
from DNA.builtins import *
from DNA.interop.System.Runtime import Notify, Base58ToAddress, Serialize, Deserialize
from DNA.interop.System.App import RegisterAppCall
from DNA.lib.require import *
from DNA.interop.System.Runtime import CheckWitness
from DNA.interop.System.Storage import GetContext, Get, Put, Delete

ListKey = "ListKey"
Name = "ListDemo"

def Main(operation, args):
    if operation =='appendList':
        msg = args[0]
        return appendList(msg)
    if operation =='getList':
        return getList()

def appendList(msg):
    listByte = getData(ListKey)
    if listByte == None:
        list = []
    else:
        list = Deserialize(listByte)
    map = {"msg" : msg}
    list.append(map) 
    setData(ListKey, Serialize(list))
    return True

def getList():
    listByte = getData(ListKey)
    if listByte == None:
        list = []
    else:
        list = Deserialize(listByte)
    res = "["
    for item in list:
        res = concat(concat(res, getMapJson(item)), ",")
    if len(res) > 1:  
        res = substr(res, 0, len(res) - 1)
    res = concat(res, "]")
    return res

def getMapJson(map):
    # mapInfo = getData(mapKey)
    # if mapInfo == None:
    #     map = {}
    # else:
    #     map = Deserialize(mapInfo)
    res = "{"
    for key in map.keys():
        res = concat(concat(concat(res,'"'), key), '":"')
        res = concat(concat(res, map[key]), '",')
    if len(res) > 1:  
        res = substr(res, 0, len(res) - 1)
    res = concat(res, "}")
    return res

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