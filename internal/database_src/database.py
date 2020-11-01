import os
import internal.block_src.block as block
import internal.block_src.block_chain as block_chain
import internal.database_src.database_action as database_action

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
            new_bc = block_chain.block_chain()
            new_block = new_bc.New_Genesis_Block()
            database_action.db_write_file(new_block)
            return new_bc
        else:
            new_bc = block_chain.block_chain()
            for f in self._db:
                if f.endswith('.txt'):
                    new_block = database_action.db_read_file(f'block_file/{f}')
                    new_bc.Add_exist_block(new_block)
        return new_bc



