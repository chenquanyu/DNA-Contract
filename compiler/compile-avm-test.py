#!/usr/bin/env python3
#
# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright 2019 DNA Dev team
# Copyright 2018 Ontology Dev team
#
from DNA.compiler import Compiler

def CompileContract():
    sc = """Cversion = '2.0.0'
from DNA.interop.System.Runtime import Log

def Main(operation, args):
    if operation == 'LogTest':
        return LogTest()
    return False

def LogTest():
    Log('Hello, world!')
    return True
"""

    try:
        avm = Compiler.Compile_Contract(sc)
        return avm
    except Exception as error:
        print("[CompileContract Error]: " + str(error))
        return ""

def CompileFile():
    try:
        avm = Compiler.Compile_File("basic-contract.py")
        return avm
    except Exception as error:
        print("[CompileFile Error]: " + str(error))
        return ""

assert CompileContract() == CompileFile(), 'Compile test failed'
