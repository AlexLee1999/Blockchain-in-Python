import time
import collections
import internal.block_src.block as block
import internal.transactions_src.transactions_actions as transactions_actions

class block_chain(object):
    def __init__(self):
        self._chain = []
        self._height = 0

    def New_Block(self, transactions, prev_block_hash, prev_height):
        new_block = block.block(prev_height + 1, prev_block_hash, time.time(), 20, 0, 0)
        new_block.add_transactions(transactions)
        new_block.set_hash_and_nonce()
        self._chain.append(new_block)
        self._height += 1
        return new_block

    def Add_exist_block(self, block):
        self._chain.append(block)
        self._height += 1
        return

    def New_Genesis_Block(self, address, wallet_set):
        new_transactions = transactions_actions.coinbase_transactions(address, wallet_set)
        new_block = self.New_Block(new_transactions, "", 0)
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


    def find_account_amount(self, address, wallet_set):
        wallet = wallet_set.find_via_address(address)
        public_key_hash = wallet.hash_public_key
        spent_txo = collections.defaultdict(list)
        unspent_txs = []
        for block in self._chain:
            for tx in block.transactions:
                if not tx.is_coinbase():
                    for vin in tx.vin:
                        if vin.hashkey(public_key_hash):
                            spent_txo[vin.txid] = vin.vout
                tx_id = tx.id
                for out_idx, out in enumerate(tx.vout):
                    if spent_txo[tx_id]:
                        for spent_out in spent_txo[tx_id]:
                            if spent_out == out_idx:
                                pass
                    if out.is_locked_with_key(public_key_hash):
                        unspent_txs.append(tx)
        print(unspent_txs)
        return unspent_txs




            

                