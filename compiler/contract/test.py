Cversion = '2.0.0'
from DNA.libont import bytearray_reverse, hexstring2bytes
from DNA.interop.System.App import RegisterAppCall, DynamicAppCall
from DNA.interop.System.Runtime import Notify, Serialize, Deserialize
from DNA.interop.System.Storage import GetContext, Get, Put, Delete
from DNA.builtins import append, remove, concat, keys

MAPKEY = "Map"

def Main(operation, args):
    if operation == "init":
        return init()
    if operation == "add_map":
        key = args[0]
        value = args[1]
        return add_map(key, value)
    if operation == "remove_map":
        key = args[0]
        return remove_map(key)
    if operation == "list_keys":
        return list_keys()
    return False

def init():
    # init map
    map1 = {
        "key1": 1,
        "key2": 2
    }
    map1Info = Serialize(map1)
    Put(GetContext(), MAPKEY, map1)
    # return result
    Notify(["init map is ", map1["key1"], map1["key2"]])

    return True


def add_map(key, value):
    map1Info = Get(GetContext(), MAPKEY)
    map1 = Deserialize(map1Info)

    Notify(["before add, map is ", map1["key1"], map1["key2"]])
    # add data 
    map1[key] = value
    map1Info = Serialize(map1)
    Put(GetContext(), MAPKEY, map1Info)
    Notify(["after add, map is ", map1["key1"], map1["key2"], map1[key]])

    return True


def remove_map(key):
    map1Info = Get(GetContext(), MAPKEY)
    map1 = Deserialize(map1Info)
    Notify(["before remove, map is ", map1["key1"], map1["key2"], map1[key]])
    map1.remove(key)
    map1Info = Serialize(map1)
    Put(GetContext(), MAPKEY, map1Info)
    Notify(["after remove, map is ", map1["key1"], map1["key2"]])
    return True

def list_keys():
    #map1Info = Get(GetContext(), MAPKEY)
    #map1 = Deserialize(map1Info)
    map1 = Get(GetContext(), MAPKEY)

    keys = map1.keys()
    res = "["
    for key in keys:
        res = concat(concat(res, key), ",")
    res = concat(res, "]")
    return res