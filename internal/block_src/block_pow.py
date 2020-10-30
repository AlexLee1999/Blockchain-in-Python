import internal.block_src.shared_func as shared_func
import sys
import time

max_nonce = sys.maxsize
target_bits = 10


class Pow(object):
    def __init__(self, block):
        self._block = block
        self._target = 1 << (256 - target_bits)

    @property
    def block(self):
        return self._block

    @property
    def target(self):
        return self._target

    def prepare_data(self, nonce):
        return f"{self.block.prevblockhash}{self.block.transactions}{target_bits}{nonce}"

    def run(self):
        nonce = 0
        while nonce < max_nonce:
            data = self.prepare_data(nonce)
            hex_out = shared_func.hash_string(data)
            hex_int = int(hex_out, 16)
            if hex_int < self.target:
                break
            else:
                nonce += 1

        return nonce, hex_out

    def validate(self):
        data = self.prepare_data(self.block.nonce)
        hex_out = shared_func.hash_string(data)
        hex_int = int(hex_out, 16)
        if hex_int < self.target:
            return True
        else:
            return False

