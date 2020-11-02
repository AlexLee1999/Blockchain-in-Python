import internal.database_src.database_action as database_action
import internal.database_src.database as database


def addblock(bc, transactions):
    if bc == None:
        print("block chain doesn't exist")
        return
    new_block = bc.New_Block(transactions, bc.get_prevblockhash(), bc.height)
    database_action.db_write_file(new_block)


def printchain(bc):
    if bc == None:
        print("block chain doesn't exist")
        return
    print(bc)


def printblock(bc, height):
    if bc == None:
        print("block chain doesn't exist")
        return
    elif len(bc.chain) < height:
        print('block does not exist')
    else:
        print(bc.chain[height - 1])


def createblockchain(address, bc, db):
    if bc != None:
        print('Block chain already exist !')
        return
    else:
        bc = db.get_new_block_chain(address)
        return bc


