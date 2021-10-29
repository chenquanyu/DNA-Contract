# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright 2019 DNA Dev team
# Copyright 2018 Ontology Dev team
#
def Require(expr, message="There was an error"):
    '''
    Raises an exception if the given expression is false.

    :param expr: The expression to evaluate.
    :param message: The error message to log.
    '''
    from DNA.interop.System.Runtime import Log
    if not expr:
        Log(message)
        raise Exception(message)


def RequireIsAddress(address):
    '''
    Raises an exception if the given address is not the correct length.

    :param address: The address to check.
    '''
    Require(len(address) == 20, "Address has invalid length")


def RequireWitness(address):
    '''
    Raises an exception if the given address is not a witness.

    :param address: The address to check.
    '''
    from DNA.interop.System.Runtime import CheckWitness
    Require(CheckWitness(address), "Address is not witness")
