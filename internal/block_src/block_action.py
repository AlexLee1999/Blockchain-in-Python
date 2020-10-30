import internal.database_src.database as database

def addblock(bc, transactions):
    new_block = bc.New_Block(transactions, bc.get_prevblockhash(), bc.height)
    database.db_write_file(new_block)


def printchain(bc):
    print(bc)


def printblock(bc, height):
    print(bc.chain[height - 1])