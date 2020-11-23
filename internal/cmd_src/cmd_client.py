import internal.block_src.block_chain as block_chain
import internal.block_src.block as block
import internal.block_src.block_pow as block_pow
import internal.database_src.database as database
import internal.database_src.database_action as database_action
import internal.cmd_src.cmd_parse as cmd_parse
import internal.block_src.block_action as block_action
import internal.wallet_src.wallet as wallet
import internal.wallet_src.wallet_set as wallet_set
import internal.database_src.db_wallet as db_wallet
import internal.utxo_src.utxo as utxo
import internal.database_src.db_utxo as db_utxo
import internal.transactions_src.transactions_actions as transactions_actions
import internal.transactions_src.transactions as transactions


class cmd_client(object):
    def __init__(self):
        self._db = database.DB()
        self._bc = None
        self._wallet_set = None
        self._wallet_db = db_wallet.DB_wallet()
        self._utxo = utxo.utxo()
        self._utxo_db = db_utxo.DB_utxo()
        if self._utxo_db.count_num() != 0:
            self._utxo = self._utxo_db.get_utxo()
        if self._db.count_num() != 0:
            self._bc = self._db.get_block_chain()
        if self._wallet_db.count_num() != 0:
            self._wallet_set = self._wallet_db.get_wallet()
        
    
    
    def command_line(self):
        while True:
            cmd = input('cmd>>>')
            action = cmd_parse.parsecmd('./psudobitcoin '+cmd)
            if action == None:
                continue
            elif 'exit' == action[0]:
                break
            elif 'printchain' == action[0]:
                block_action.printchain(self._bc)
            elif 'printblock' == action[0]:
                block_action.printblock(self._bc, int(action[1]))
            elif 'createblockchain' == action[0]:
                self._bc = block_action.createblockchain(action[1], self._bc, self._db, self._wallet_set, self._utxo)
            elif 'createwallet' == action[0]:
                if self._wallet_set == None:
                    self._wallet_set = wallet_set.wallet_set()
                new_wallet = wallet.wallet(None, None, None, None)
                self._wallet_set.add_wallet(new_wallet)
                print(new_wallet)
                database_action.db_wallet_write_file(new_wallet)
            elif 'getbalance' == action[0]:
                w = self._wallet_set.find_via_address(action[1])
                s = self._utxo.find_funds(w.hash_public_key)
                print(f"Your Balance :{s}")
            elif 'send' == action[0]:
                new_t = transactions_actions.new_transactions(action[1], action[2], action[3], self._bc, self._wallet_set, self._utxo)
                if new_t != None:
                    new_block = self._bc.mine(new_t, action[1], self._wallet_set)

                    self._utxo.update(new_block)
                
                    
