import internal.block_src.block as block
import internal.block_src.block_chain as block_chain
import internal.wallet_src.wallet as wallet
import internal.wallet_src.wallet_set as wallet_set
import internal.transactions_src.transactions as transactions
import internal.transactions_src.txinput as txinput
import internal.transactions_src.txoutput as txoutput
import internal.utxo_src.utxo as utxo
import json
import pickle

def db_read_file(filename):
    with open(f'{filename}', 'rb') as handle:
        b = pickle.load(handle)
    return b


def db_write_file(block):
    with open('block_file/%04d.db'% block.height, 'wb') as handle:
        pickle.dump(block, handle, protocol=pickle.HIGHEST_PROTOCOL)

def db_wallet_read_file(filename):
    with open(f'{filename}', 'rb') as handle:
        b = pickle.load(handle)
    return b


def db_wallet_write_file(wallet):
    with open('wallet_file/%s.db'% wallet.address, 'wb') as handle:
        pickle.dump(wallet, handle, protocol=pickle.HIGHEST_PROTOCOL)

def db_utxo_read_file():
    with open('utxo_file/utxo.db', 'rb') as handle:
        b = pickle.load(handle)
    new_utxo = utxo.utxo(set=b)
    return new_utxo

def db_utxo_write_file(s):
    with open('utxo_file/utxo.db', 'wb') as handle:
        pickle.dump(s, handle, protocol=pickle.HIGHEST_PROTOCOL)

