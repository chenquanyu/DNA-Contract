<p align="center">
  Python SmartContract Compiler for DNA
</p>

- Free software: LGPL license
  - [Overview](#Overview)
  - [Installation](#Installation)
  - [Usage](#Usage)
  - [License](#License)
  - [DebugInfo](#DebugInfo)

## Overview

Official python smart contract compiler to compile Python files to the `.avm` format for usage in smart contracts on the [DNA blockchain](https://github.com/DNAProject/DNA/). It currently only supports a subset of the Python language.

#### What does it currently do

- Compiles a subset of the Python language to the `.avm` format for use in the [DNA blockchain](https://github.com/DNAProject/DNA)
- Works for Python 3.6+

#### What will it do

- Compile a larger subset of the Python language
- Additional syntax checks
- Optimize instr stream

## Installation

Installation requires Python version 3.6 or later.

#### Setup

Clone the repository and navigate into the project directory. Make a Python 3 virtual environment and activate it via:

```
python3 -m venv venv
source venv/bin/activate
```

Then, install the requirements:

```
pip install -r requirements.txt
```

## Usage

Import the compiler into a file with:
```
from DNA.compiler import Compiler
```

The compiler can be used in three different ways:

1) Compiling a python file to a new file
```
# Compiles the python file and creates an avm in 'path/to/your/file.avm'.
compiler = Compiler.Compile('path/to/your/file.py')
```

2) Compiling a python file to `.avm`
```
# Compiles the python file and returns an avm.
avm = Compiler.Compile_File('path/to/your/file.py')
```

3) Compiling a variable to `.avm`
```
# Compiles a contract stored in memory and returns an avm.
avm = Compiler.Compile_Contract('def Main(operation, args): ...')
```

You can also print out the instr instream:
```
compiler.DumpAsm()
```

#### CLI

You can use the following command line to compile DNA python smart contract.

```
python3 run.py -n <smart-contract.py>
```

#### Testing

You can run the tests using the ```runall.bash``` or ```runall-testing.bash``` files located in ```DNA_test```. You can run the compiler tests using the `compile-avm-test.py` file in the root directory.

## Contributing

Contributors are welcome to the `DNA-python-compiler`. Before beginning, please take a look at our [contributing guidelines](./CONTRIBUTING.md). You can open an issue by [clicking here](https://github.com/DNAProject/DNA-python-compiler/issues/new).


## License

- Open-source [LGPL](LICENSE).
- Main author is [@steven](https://github.com/carltraveler)

## DebugInfo

FuncName:   indicate the opcode blongs to which function. Global#Code is for Code in Global.

Lineno:          indicate the opcode blongs to which line number in source code.

Col :               indicate the opcode blongs to which columns in source code.

offset:            the address of Opcode. from 0 to len of avm.

Opcode:        the Opcode.

JumpTarget:  the target address(offset) of jump instruct.

TargetOff:      the relative offset between target address and current jump instruction.  	 	      

```
FuncName                       Lineno     Col   Offset     OpCode               JumpTarget           TargetOff           
Global#Code                    1          0     0          PUSH2               
Global#Code                    1          0     1          NEWARRAY            
Global#Code                    1          0     2          TOALTSTACK          
Global#Code                    1          14    3          PUSHBYTES5          
Global#Code                    1          0     9          DUPFROMALTSTACK     
Global#Code                    1          0     10         PUSH0               
Global#Code                    1          0     11         PUSH2               
Global#Code                    1          0     12         ROLL                
Global#Code                    1          0     13         SETITEM             
Global#Code                    3          4     14         PUSH2               
Global#Code                    3          0     15         DUPFROMALTSTACK     
Global#Code                    3          0     16         PUSH1               
Global#Code                    3          0     17         PUSH2               
Global#Code                    3          0     18         ROLL                
Global#Code                    3          0     19         SETITEM             
Global#Code                    4          0     20         FROMALTSTACK        
Main                           4          0     21         PUSH3               
Main                           4          0     22         NEWARRAY            
Main                           4          0     23         TOALTSTACK          
Main                           4          0     24         DUPFROMALTSTACK     
Main                           4          0     25         PUSH0               
Main                           4          0     26         PUSH2               
Main                           4          0     27         ROLL                
Main                           4          0     28         SETITEM             
Main                           5          8     29         PUSH0               
Main                           5          4     30         DUPFROMALTSTACK     
Main                           5          4     31         PUSH1               
Main                           5          4     32         PUSH2               
Main                           5          4     33         ROLL                
Main                           5          4     34         SETITEM             
Main                           6          8     35         DUPFROMALTSTACK     
Main                           6          8     36         PUSH0               
Main                           6          8     37         PICKITEM            
Main                           6          8     38         CALL                 49                   11    
```
