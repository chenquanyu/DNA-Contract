# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright 2019 DNA Dev team
# Copyright 2018 Ontology Dev team
#
def GetScriptContainer():
    """
    Returns the current Script Container of a smart contract execution.
    This will be a ``DNA.blockchain.vm.DNA.Transaction`` object.

    - Note: This method is implemented inside the DNA Virtual Machine.

    :return: the current ScriptContainer of a smart contract execution.
    :rtype: ``DNA.blockchain.vm.DNA.Transaction``
    """
    pass


def GetExecutingScriptHash():
    """
    Returns the hash of the script ( smart contract ) which is currently being executed

    - Note: This method is implemented inside the DNA Virtual Machine.

    :return: the hash of the script ( smart contract ) which is currently being executed
    :rtype: bytearray
    """
    pass


def GetCallingScriptHash():
    """
    Returns the hash of the script ( smart contract ) which began execution of the current script.

    - Note: This method is implemented inside the DNA Virtual Machine.

    :return: the hash of the script ( smart contract ) which began execution of the current script
    :rtype: bytearray
    """
    pass


def GetEntryScriptHash():
    """
    Returns the hash of the script ( smart contract ) which began execution of the smart contract.

    - Note: This method is implemented inside the DNA Virtual Machine.

    :return: the hash of the script ( smart contract ) which began execution of the smart contract
    :rtype: bytearray
    """
    pass
