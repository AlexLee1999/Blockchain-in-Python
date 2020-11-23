import time
import internal.block_src.block_pow as pow
import internal.merkle_src.merkle as merkle


class block(object):
    def __init__(self, height, prevblockhash, time, bits, nonce, hash):
        self._height = height
        self._prevblockhash = prevblockhash
        self._time = time
        self._bits = bits
        self._nonce = nonce
        self._transactions = []
        self._hash = hash
        self._merkle_root = None

    def __repr__(self):
        return f"Height: {self.height}, prevblockhash: {self.prevblockhash}, time: {self.time}, bits: {self.bits}, nonce: {self.nonce}, transactions: {self.transactions}, hash: {self.hash}, merkle root: {self._merkle_root}\n"

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
        new_pow = pow.Pow(self)
        nonce, hash = new_pow.run()
        self._nonce = nonce
        self._hash = hash
        self._merkle_root = self.hash_transactions()
        return

    def add_transactions(self, t):
        self.transactions.append(t)

    def hash_transactions(self):
        tx_lst = []
        for tx in self._transactions:
            tx_lst.append(tx)
        m_tree = merkle.MerkleTree(tx_lst)
        return m_tree.root_hash

