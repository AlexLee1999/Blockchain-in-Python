import time
from .block_pow import Pow

class block(object):
    def __init__(self, height, prevblockhash, time, bits, nonce, transactions, hash):
        self._height = height
        self._prevblockhash = prevblockhash
        self._time = time
        self._bits = bits
        self._nonce = nonce
        self._transactions = transactions
        self._hash = hash

    def __repr__(self):
        return f"Height: {self.height}, prevblockhash: {self.prevblockhash}, time: {self.time}, bits: {self.bits}, nonce: {self.nonce}, transactions: {self.transactions}, hash: {self.hash}\n"
    
    @property
    def height(self):
        return self._height

    @property
    def prevblockhash(self):
        return self._prevblockhash

    @property
    def time(self):
        return self._time
    
    @property
    def bits(self):
        return self._bits

    @property
    def nonce(self):
        return self._nonce
    
    @property
    def transactions(self):
        return self._transactions
    
    @property
    def hash(self):
        return self._hash

    def set_hash_and_nonce(self):
        new_pow = Pow(self)
        nonce, hash = new_pow.run()
        self._nonce = nonce
        self._hash = hash
        return
        





