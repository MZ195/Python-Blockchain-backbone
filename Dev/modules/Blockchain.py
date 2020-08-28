import uuid
from hashlib import sha256
import json
from time import time

class Blockchain(object):
    def __init__(self):
        #  This array will hold all verified blocks
        self.chain = [] 
        #  this array will hold a list of transactions before they are placed in a block and mined
        self.pendingTransactions = []
        #  genesis block
        self.createNewBlock(100, '0', '0')
        #  the url of the hosting node
        self.currentNodeURL = str(uuid.uuid1()).replace('-', '')
        #  the list of all nodes in the network
        self.networkNodes = []

    def createNewBlock(self, nonce, previousBlockHash, hash):
        newBlock = {
            "index": len(self.chain) + 1,
            "timestamp": time,
            "transactions": self.pendingTransactions,
            "nonce": nonce,
            "hash": hash,
            "previousBlockHash": previousBlockHash
        }
        self.pendingTransactions = []
        self.chain.append(newBlock)
        return newBlock


    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def createNewTransaction(self, amount, sender, recipient):
        #  we need unique ID for each transaction
        newTransaction = {
            "amount": amount,
            "sender": sender,
            "recipient": recipient,
            "transactionId": str(uuid.uuid1()).replace('-', '')
        }
        return newTransaction

    def addTransactionToPendingTransactions(self, transactionObj):
        self.pendingTransactions.append(transactionObj)
        result = self.getLastBlock['index'] + 1
        return result

    def hashBlock(self, previousBlockHash, currentBlockData, nonce):
        dataAsString = previousBlockHash + json.stringify(currentBlockData) + nonce.toString()
        hash = sha256(dataAsString)
        return hash

    def proofOfWork(self, previousBlockHash, currentBlockData):
        #  repeatedly hash the block until it finds correct hash => '00004dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        #  uses current block data and previous block hash to compute the new hash
        #  continouusly changes the nonce value until it finds the correct hash
        #  returns the nonce value that produced the correct hash

        nonce = 0
        hash = self.hashBlock(previousBlockHash, currentBlockData, nonce)

        while(hash.substring(0, 4) != '0000'):
            nonce =+ 1
            hash = self.hashBlock(previousBlockHash, currentBlockData, nonce)

        return nonce

    def chainIsValid(self, blockchain):
        validChain = True
        # we need to use for loop so that we can access current and front blocks
        for i in range(len(blockchain)):
            currentBlock = blockchain[i]
            previousBlock = blockchain[i - 1]
            blockHash = self.hashBlock(previousBlock['hash'], {"transactions": currentBlock['transactions'], "index": currentBlock['index']}, currentBlock['nonce'])
            
            # hashing every block and make sure it starts with 4 0s
            if(blockHash.substring(0, 4) != '0000'):
                validChain = False
            
            # making sure the hashes align
            if(currentBlock['previousBlockHash'] != previousBlock['hash']):
                validChain = False

            # since we created the genesis block ourselves we should validate it.
            # it is critical to create a unique one
            genesisBlock = blockchain[0]
            correctNonce = genesisBlock['nonce'] == 100
            correctPreviousblockHash = genesisBlock['previousBlockHash'] == '0'
            correctHash = genesisBlock['hash'] == '0'
            correctTransactions = genesisBlock['transactions'].length == 0

            if(not correctNonce or (not correctPreviousblockHash) or (not correctHash) or (not correctTransactions)):
                validChain = False

        return validChain

    # we implemented it this way to handel the case if the hash does not exists
    def getBlock(self, blockHash):
        for block in self.chain:
            if(block["hash"] == blockHash):
                return block
        
        return None

    # I don't like the performance of this one
    # I should be able to get the data using hashing
    def getTransaction(self, transactionId):
        for block in self.chain:
            for transaction in block:
                if(transaction.transactionId == transactionId):
                    return {
                        "transaction": transaction,
                        "block": block 
                    }
        return None

    # I don't like the performance of this one
    # I should be able to get the data using hashing
    def getAddressData(self, address):
        addressTransactions = []

        for block in self.chain:
            for transaction in block:
                if(transaction.sender == address or transaction.recipient == address):
                    addressTransactions.append(transaction)

        balance = 0
        for transaction in addressTransactions:
            if(transaction.recipient == address):
                balance += transaction.amount
            else:
                balance -= transaction.amount
            
        
        return {
            "addressTransactions": addressTransactions,
            "addressBalance": balance
        }
