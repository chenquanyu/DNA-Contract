Cversion = '2.0.0'
from DNA.interop.System.Block import GetTransactionByIndex
from DNA.interop.System.Blockchain import GetTransactionByHash
from DNA.interop.System.Header import GetBlockHash
from DNA.interop.System.Transaction import GetTransactionHash
from DNA.interop.System.Blockchain import GetBlock


def main(Height):
    Block = GetBlock(Height)
    index = 0
    Tx = GetTransactionByIndex(Block, index)
    Txhash = GetTransactionHash(Tx)
    NewTx = GetTransactionByHash(Txhash)
    BlkHash = GetBlockHash(Block)
    print("Test finished")
