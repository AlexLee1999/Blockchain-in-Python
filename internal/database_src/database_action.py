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
    f = open(filename)
    height = f.readline()
    height = height[:-1]
    height = int(height)
    prevblockhash = f.readline()
    prevblockhash = prevblockhash[:-1]
    time = f.readline()
    time = time[:-1]
    bits = f.readline()
    bits = bits[:-1]
    nonce = f.readline()
    nonce = nonce[:-1]
    nonce = int(nonce)
    trans = f.readline()
    trans = trans[:-1]
    dic = json.loads(trans)
    id = dic['id']
    new_tra = transactions.transactions(id)
    vin = dic['vin']
    vout = dic['vout']
    for v in vin:
        j = json.loads(v)
        new_in = txinput.txinput(j['_txid'], j['_vout'], j['_sig'], j['_public_key'])
        new_tra.add_vin(new_in)
    for v in vout:
        j = json.loads(v)
        new_out = txoutput.txoutput(j['_value'], j['_public_key_hash'])
        new_tra.add_vout(new_out)
    hash = f.readline()
    b = block.block(height, prevblockhash, time, bits, nonce, hash)
    b.add_transactions(new_tra)
    return b


def db_write_file(block):
    f = open(f'block_file/%04d.txt' % block.height, 'w')
    f.write(f"{block.height}\n")
    f.write(f"{block.prevblockhash}\n")
    f.write(f"{block.time}\n")
    f.write(f"{block.bits}\n")
    f.write(f"{block.nonce}\n")
    for t in block.transactions:
        f.write(f"{t.set_json()}\n")
    f.write(f"{block.hash}")

def db_wallet_read_file(filename):
    f = open(filename)
    private = f.readline()
    private = private[:-1]
    public = f.readline()
    public = public[:-1]
    hash_public_key = f.readline()
    hash_public_key = hash_public_key[:-1]
    address = f.readline()
    return wallet.wallet(private, public, hash_public_key, address)


def db_wallet_write_file(wallet):
    f = open(f'wallet_file/%s.txt' % wallet.address, 'w')
    f.write(f"{wallet.private_key}\n")
    f.write(f"{wallet.public_key}\n")
    f.write(f"{wallet.hash_public_key}\n")
    f.write(f"{wallet.address}")

def db_utxo_read_file():
    with open('utxo_file/utxo.db', 'rb') as handle:
        b = pickle.load(handle)
    new_utxo = utxo.utxo(set=b)
    return new_utxo

def db_utxo_write_file(s):
    with open('utxo_file/utxo.db', 'wb') as handle:
        pickle.dump(s, handle, protocol=pickle.HIGHEST_PROTOCOL)

