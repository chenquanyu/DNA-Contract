Cversion = '2.0.0'
from DNA.interop.System.Runtime import Notify
from DNA.builtins import concat

def Main(operation, args):
    if operation =='hello':
        msg = args[0]
        return hello(msg)

def hello(msg):
    Notify(msg)
    return concat('Hello ', msg)