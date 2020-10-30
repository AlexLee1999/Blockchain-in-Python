from internal.block_src import block_chain
from internal.block_src import block
from internal.block_src import block_pow
from internal.database import database
from internal.cmd_src import cmd_parse

import sys

def command_line():
    while True:
        cmd = input('cmd>>>')
        action = cmd_parse.parsecmd('./psudobitcoin '+cmd)
        if action == None:
            continue
        elif 'exit' == action[0]:
            break
        elif 'addblock' == action[0]:
            addblock(new_bc, action[1])
        elif 'printchain' == action[0]:
            printchain(new_bc)
        elif 'printblock' == action[0]:
            printblock(new_bc, int(action[1]))



def addblock(bc, transactions):
    new_block = bc.New_Block(transactions, bc.get_prevblockhash(), bc.height)
    database.db_write_file(new_block)

def printchain(bc):
    print(bc)

def printblock(bc, height):
    print(bc.chain[height - 1])




if __name__ == "__main__":
    new_db = database.DB()
    new_bc = new_db.get_block_chain()
    
    command_line()
    
