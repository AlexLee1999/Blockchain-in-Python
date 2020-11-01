import time
import internal.block_src.block as block


class block_chain(object):
    def __init__(self):
        self._chain = []
        self._height = 0

    def New_Block(self, transactions, prev_block_hash, prev_height):
        new_block = block.block(prev_height + 1, prev_block_hash, time.time(), 20, 0, transactions, 0)
        new_block.set_hash_and_nonce()
        self._chain.append(new_block)
        self._height += 1
        return new_block

    def Add_exist_block(self, block):
        self._chain.append(block)
        self._height += 1
        return

    def New_Genesis_Block(self):
        new_block = self.New_Block("New Genesis Block", "", 0)
        return new_block

    def get_prevblockhash(self):
        return (self._chain)[-1].hash

    def __repr__(self):
        result = ""
        for block in self._chain:
            result += f" >> {block}\n"
        return result

    @property
    def height(self):
        return self._height

    @property
    def chain(self):
        return self._chain

