import uuid
from hashlib import sha256
import json
from time import time

class Transaction(object):
    def __init__(self, amount, sender, recipient):
        #  This array will hold all verified blocks
        self.amount = amount
        #  this array will hold a list of transactions before they are placed in a block and mined
        self.sender = sender
        #  genesis block
        self.recipient = recipient
        #  the url of the hosting node
        self.transactionId = str(uuid.uuid1()).replace('-', '')

    def to_json(self):
        data = []
        data['amount'] = self.amount
        data['sender'] = self.sender
        data['recipient'] = self.recipient
        data['transactionId'] = self.transactionId

        return data