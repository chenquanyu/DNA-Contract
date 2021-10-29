"""
An Example of OEP-4
"""
from DNA.interop.System.Storage import GetContext, Get, Put, Delete
from DNA.interop.System.Runtime import Notify, CheckWitness
from DNA.interop.System.Action import RegisterAction
from DNA.builtins import concat
from DNA.builtins import *
TransferEvent = RegisterAction("transfer", "from", "to", "amount")
ApprovalEvent = RegisterAction("approval", "owner", "spender", "amount")
from DNA.interop.DNA.Runtime import Base58ToAddress
ctx = GetContext()

FACTOR = 100000000
OWNER = Base58ToAddress("AQf4Mzu1YJrhz9f3aRkkwSm9n3qhXGSh4p")
TOTAL_AMOUNT = 1000000000
BALANCE_PREFIX = "_BALANCE__"
APPROVE_PREFIX = "_APPROVE__"
SUPPLY_KEY = 'TotalSupply'

def Main(operation, args):
    if operation == 'init':
        return init(args)
    if operation == 'balanceOf':
        if len(args) != 1:
            return False
        acct = args[0]
        return balanceOf(acct)
    if operation == 'transfer':
        if len(args) != 3:
            return False
        else:
            from_acct = args[0]
            to_acct = args[1]
            amount = args[2]
            return transfer(from_acct, to_acct, amount)
    return False

def init(args):
    if Get(ctx, SUPPLY_KEY):
        Notify("Already initialized!")
        return False
    else:
        air_num = Airdrop(args)
        total = TOTAL_AMOUNT * FACTOR
        Require(total > air_num)
        Put(ctx, SUPPLY_KEY, total)
        Put(ctx, concat(BALANCE_PREFIX, OWNER), total - air_num)

        TransferEvent("", OWNER, total)
        return True

def balanceOf(account):
    return Get(ctx, concat(BALANCE_PREFIX, account))


def transfer(from_acct, to_acct, amount):
    if not CheckWitness(from_acct):
        return False

    Require(amount > 0)
    fromKey = concat(BALANCE_PREFIX, from_acct)
    fromBalance = Get(ctx, fromKey)
    if amount > fromBalance:
        return False
    if amount == fromBalance:
        Delete(ctx, fromKey)
    else:
        Put(ctx, fromKey, fromBalance - amount)

    toKey = concat(BALANCE_PREFIX, to_acct)
    toBalance = Get(ctx, toKey)
    Put(ctx, toKey, toBalance + amount)

    TransferEvent(from_acct, to_acct, amount)
    return True


def approve(owner, spender, amount):
    if not CheckWitness(owner):
        return False
    key = concat(concat(APPROVE_PREFIX, owner), spender)
    Put(ctx, key, amount)

    ApprovalEvent(owner, spender, amount)
    return True

def Revert():
    """
    Revert the transaction. The opcodes of this function is `09f7f6f5f4f3f2f1f000f0`,
    but it will be changed to `ffffffffffffffffffffff` since opcode THROW doesn't
    work, so, revert by calling unused opcode.
    """
    raise Exception(0xF1F1F2F2F3F3F4F4)


"""
https://github.com/ONT-Avocados/python-template/blob/master/libs/SafeCheck.py
"""
def Require(condition):
    """
	If condition is not satisfied, return false
	:param condition: required condition
	:return: True or false
	"""
    if not condition:
        Revert()
    return True

def Airdrop(args):
    airdrop_num = 0
    for p in args:
        if len(p) != 2:
            raise Exception('Airdrop failed - input error!')
        toKey = concat(BALANCE_PREFIX, p[1])
        Put(ctx, toKey, p[1])
        airdrop_num = p[1] + airdrop_num
    return airdrop_num
