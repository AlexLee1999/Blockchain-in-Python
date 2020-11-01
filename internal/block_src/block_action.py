import internal.database_src.database_share_func as database_share_func

def addblock(bc, transactions):
    new_block = bc.New_Block(transactions, bc.get_prevblockhash(), bc.height)
    database_share_func.db_write_file(new_block)


def printchain(bc):
    print(bc)


def printblock(bc, height):
    print(bc.chain[height - 1])