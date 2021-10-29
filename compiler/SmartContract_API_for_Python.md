| Package | Name | Parameter |      |
| ---- | ---- | ---- | ---- |
|           DNA.interop.DNA.Attribute |                  GetUsage |                                   transaction_attr | get transaction attribute usage |
|           DNA.interop.DNA.Attribute |                   GetData |                                   transaction_attr | get transaction attribute data |
|            DNA.interop.DNA.Contract |                 GetScript |                                           contract | get contract script hash |
|            DNA.interop.DNA.Contract |                    Create | script, parameter_list, return_type, properties, name, version, author, email, description | create a contract |
|            DNA.interop.DNA.Contract |                   Migrate | script, parameter_list, return_type, properties, name, version, author, email, description | migrate  contract |
|              DNA.interop.DNA.Header |                GetVersion |                                             header | get the version of header |
|              DNA.interop.DNA.Header |             GetMerkleRoot |                                             header | get the merkle root of the transactions contained in the block |
|              DNA.interop.DNA.Header |          GetConsensusData |                                             header | get the address of the consensus |
|              DNA.interop.DNA.Header |          GetNextConsensus |                                             header | get the address where the next consensus will occur |
|              DNA.interop.DNA.Native |                    Invoke |                   param,method,contractAddress,ver | invoke native contract |
|             DNA.interop.DNA.Runtime |           Base58ToAddress |                                                arg | transfer base58 address to byte array |
|             DNA.interop.DNA.Runtime |           AddressToBase58 |                                                arg | byte array address to base58 |
|             DNA.interop.DNA.Runtime | GetCurrentBlockHash |                                                    | get current block hash |
|         DNA.interop.DNA.Transaction |                   GetType |                                        transaction | get transaction type |
|         DNA.interop.DNA.Transaction |             GetAttributes |                                        transaction | get transaction attributes |
|                DNA.interop.System.Action |            RegisterAction |                                  event_name, *args | register a notirfy event |
|                   DNA.interop.System.App |           RegisterAppCall |                         smart_contract_hash, *args | call other smart contract |
|            DNA.interop.System.Blockchain |                 GetHeight |                                                    | get height of block chain |
|            DNA.interop.System.Blockchain |                 GetHeader |                                     height_or_hash | get header by height or hash |
|            DNA.interop.System.Blockchain |                  GetBlock |                                     height_or_hash | get block by height or hash |
|            DNA.interop.System.Blockchain | GetTransactionByHash |                                               hash | get transaction by hash |
|            DNA.interop.System.Blockchain |               GetContract |                                        script_hash | get contract by script hash |
| DNA.interop.System.Blockchain | GetTransactionHeight | heigh of transaction |  |
|                 DNA.interop.System.Block |       GetTransactionCount |                                              block | get transaction count of block |
|                 DNA.interop.System.Block |           GetTransactions |                                              block | get transactions of block |
|                 DNA.interop.System.Block | GetTransactionByIndex |                                       block, index | get the transaction by index |
|              DNA.interop.System.Contract |         GetStorageContext |                                           contract | get contract storage context |
|              DNA.interop.System.Contract |                   Destroy |                                                    | destroy current contract(self) |
|       DNA.interop.System.ExecutionEngine |        GetScriptContainer |                                                    | get the current script container of a smart contract execution |
|       DNA.interop.System.ExecutionEngine |    GetExecutingScriptHash |                                                    | get the hash of the script ( smart contract ) which is currently being executed |
|       DNA.interop.System.ExecutionEngine |      GetCallingScriptHash |                                                    | get the hash of the script ( smart contract ) which began execution of the current script. |
|       DNA.interop.System.ExecutionEngine |        GetEntryScriptHash |                                                    | get the hash of the script ( smart contract ) which began execution of the smart contract. |
|                DNA.interop.System.Header |                  GetIndex |                                             header | get the height/index of header |
|                DNA.interop.System.Header |       GetBlockHash |                                             header | get the hash of header |
|                DNA.interop.System.Header |               GetPrevHash |                                             header | get the hash of the previous header in the blockchain        |
|                DNA.interop.System.Header |              GetTimestamp |                                             header | get the timestamp of when the header was created |
|               DNA.interop.System.Runtime |              CheckWitness |                                     hash_or_pubkey | check the witness of address |
|               DNA.interop.System.Runtime |                       Log |                                            message | print log on node |
|               DNA.interop.System.Runtime |                    Notify |                                                arg | add notify to event |
|               DNA.interop.System.Runtime |                   GetTime |                                                    | get timestamp of most recent block |
|               DNA.interop.System.Runtime |                 Serialize |                                               item | serialize item to byte array |
|               DNA.interop.System.Runtime |               Deserialize |                                               item | deserialize byte array to item |
|        DNA.interop.System.StorageContext |                AsReadOnly |                                                    | Convert Storage Context to ReadOnly |
|               DNA.interop.System.Storage |                GetContext |                                                    | get the storage context |
|               DNA.interop.System.Storage |        GetReadOnlyContext |                                                    | get the readOnly Storage Context |
|               DNA.interop.System.Storage |                       Get |                                       context, key | get the storage by key |
|               DNA.interop.System.Storage |                       Put |                                context, key, value | put the key-value storage |
|               DNA.interop.System.Storage |                    Delete |                                       context, key | delete storage by key |
|           DNA.interop.System.Transaction | GetTransactionHash |                                        transaction | Get the Transaction of hash |



