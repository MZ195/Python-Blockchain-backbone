import uuid
from hashlib import sha256
import json
from time import time


class Block(object):
    def __init__(self, index, nonce, transactions, hash, previousBlockHash):
        #  This array will hold all verified blocks
        self.index = index
        #  this array will hold a list of transactions before they are placed in a block and mined
        self.transactions = transactions
        #  genesis block
        self.nonce = nonce
        #  the url of the hosting node
        self.hash = hash
        #  the list of all nodes in the network
        self.previousBlockHash = previousBlockHash

    def to_json(self):
        data = []
        data['index'] = self.index
        data['transactions'] = []
        for i, transaction in enumerate(transaction):
            data['transactions'][i] = transaction.to_json()
        data['nonce'] = self.nonce
        data['previousBlockHash'] = self.previousBlockHash