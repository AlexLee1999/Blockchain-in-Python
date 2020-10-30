from ..block_src.block import *
from ..block_src.block_chain import *

import os


class DB(object):
    def __init__(self):
        self._db = os.listdir('block_file/')
        self.sortdb()

    def sortdb(self):
        self._db.sort()

    def count_num(self):
        count = 0
        for file in self._db:
            if file.endswith('.txt'):
                count += 1
        return count

    @property
    def db(self):
        return self._db
  
    def get_block_chain(self):
        if not self.count_num():
            return block_chain()
        else:
            new_bc = block_chain()
            for f in self._db:
                if f.endswith('.txt'):
                    new_block = db_read_file(f'block_file/{f}')
                    new_bc.Add_exist_block(new_block)
        return new_bc

def db_read_file(filename):
    f = open(filename)
    height = f.readline()
    height = height[:-1]
    height = int(height)
    prevblockhash = f.readline()
    prevblockhash = prevblockhash[:-1]
    time = f.readline()
    time = time[:-1]
    bits = f.readline()
    bits = bits[:-1]
    nonce = f.readline()
    nonce = nonce[:-1]
    nonce = int(nonce)
    transactions = f.readline()
    transactions = transactions[:-1]
    hash = f.readline()
    return block(height, prevblockhash, time, bits, nonce, transactions, hash)

def db_write_file(block):
    f = open(f'block_file/%04d.txt' %block.height, 'w')
    f.write(f"{block.height}\n")
    f.write(f"{block.prevblockhash}\n")
    f.write(f"{block.time}\n")
    f.write(f"{block.bits}\n")
    f.write(f"{block.nonce}\n")
    f.write(f"{block.transactions}\n")
    f.write(f"{block.hash}")
    
