import os
import ast
import internal.utxo_src.utxo as utxo
import internal.database_src.database_action as database_action
class DB_utxo(object):
    def __init__(self):
        self._db = os.listdir('utxo_file/')
        self.sortdb()

    def sortdb(self):
        self._db.sort()

    def count_num(self):
        count = 0
        for file in self._db:
            if file.endswith('.db'):
                count += 1
        return count

    @property
    def db(self):
        return self._db

    def get_utxo(self):
        new_utxo = utxo.utxo()
        new_utxo = database_action.db_utxo_read_file()
        return new_utxo