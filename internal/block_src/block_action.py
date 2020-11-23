import internal.database_src.database_action as database_action
import internal.database_src.database as database



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


def createblockchain(address, bc, db, wallet_set, utxo):
    if bc != None:
        print('Block chain already exist !')
        return
    else:
        bc = db.get_new_block_chain(address, wallet_set, utxo)
        return bc


