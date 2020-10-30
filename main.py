import internal.block_src.block_chain as block_chain
import internal.block_src.block as block
import internal.block_src.block_pow as block_pow
import internal.database_src.database as database
import internal.cmd_src.cmd_parse as cmd_parse
import internal.block_src.block_action as block_action
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
            block_action.addblock(new_bc, action[1])
        elif 'printchain' == action[0]:
            block_action.printchain(new_bc)
        elif 'printblock' == action[0]:
            block_action.printblock(new_bc, int(action[1]))


if __name__ == "__main__":
    new_db = database.DB()
    new_bc = new_db.get_block_chain()
    command_line()
    
