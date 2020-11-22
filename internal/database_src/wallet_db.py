import os
import internal.block_src.block as block
import internal.block_src.block_chain as block_chain
import internal.database_src.database_action as database_action
import internal.wallet_src.wallet_set as wallet_set


class DB_wallet(object):
    def __init__(self):
        self._db = os.listdir('wallet_file/')
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

    def get_wallet(self):
        new_wallet_set = wallet_set.wallet_set()
        for f in self._db:
            if f.endswith('.txt'):
                new_wallet = database_action.db_wallet_read_file(f'wallet_file/{f}')
                new_wallet_set.add_wallet(new_wallet)
        return new_wallet
