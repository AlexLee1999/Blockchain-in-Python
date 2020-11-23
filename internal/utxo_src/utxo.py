import internal.database_src.database_action as database_action
import json
import collections


class utxo(object):
    def __init__(self, set = dict()):
        self._set = set
    @property
    def set(self):
        return self._set

    def update(self, block):
        for tx in block.transactions:
            if not tx.is_coinbase():
                for vin in tx.vin:
                    update = []
                    outs = self._set[vin.txid]
                    for out_idx, out in enumerate(outs):
                        if out_idx != vin.vout:
                            update.append(out)
                    if len(update) == 0:
                        self._set.pop(vin.txid)
                    else:
                        self._set[vin.txid] = update
            new_outputs = [out for out in tx.vout]
            self._set[tx.id] = new_outputs
            database_action.db_utxo_write_file(self._set)
    
    def find_spendable_outputs(self, pubkey_hash, amount):
        accumulated = 0
        unspent_outputs = collections.defaultdict(list)
        for tx_id in self.set:
            outs = self.set[tx_id]
            for out_idx, out in enumerate(outs):
                if out.is_locked_with_key(pubkey_hash) and accumulated < amount:
                    accumulated += out.value
                    unspent_outputs[tx_id].append(out_idx)
        return accumulated, unspent_outputs

    def find_funds(self, pubkey_hash):
        accumulated = 0
        for tx_id in self.set:
            outs = self.set[tx_id]
            for _, out in enumerate(outs):
                if out.is_locked_with_key(pubkey_hash):
                    accumulated += out.value
        return accumulated

    def __repr__(self):
        return f"{self._set}"
