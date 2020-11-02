import internal.block_src.block_chain as block_chain
import internal.block_src.block as block
import internal.block_src.block_pow as block_pow
import internal.database_src.database as database
import internal.cmd_src.cmd_parse as cmd_parse
import internal.block_src.block_action as block_action
import sys

class client(object):
    def __init__(self):
        self._db = database.DB()
        self._bc = None
        if self._db.count_num() != 0:
            self._bc = self._db.get_block_chain()
    
    
    def command_line(self):
        while True:
            cmd = input('cmd>>>')
            action = cmd_parse.parsecmd('./psudobitcoin '+cmd)
            if action == None:
                continue
            elif 'exit' == action[0]:
                break
            elif 'addblock' == action[0]:
                block_action.addblock(self._bc, action[1])
            elif 'printchain' == action[0]:
                block_action.printchain(self._bc)
            elif 'printblock' == action[0]:
                block_action.printblock(self._bc, int(action[1]))
            elif 'createblockchain' == action[0]:
                self._bc = block_action.createblockchain(action[1], self._bc, self._db)



if __name__ == "__main__":
    cli = client()
    cli.command_line()
    
