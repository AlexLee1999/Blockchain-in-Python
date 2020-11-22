import internal.block_src.block as block
import internal.block_src.block_chain as block_chain
import internal.wallet_src.wallet as wallet
import internal.wallet_src.wallet_set as wallet_set


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
    transactions = f.readline()
    transactions = transactions[:-1]
    hash = f.readline()
    return block.block(height, prevblockhash, time, bits, nonce, transactions, hash)


def db_write_file(block):
    f = open(f'block_file/%04d.txt' % block.height, 'w')
    f.write(f"{block.height}\n")
    f.write(f"{block.prevblockhash}\n")
    f.write(f"{block.time}\n")
    f.write(f"{block.bits}\n")
    f.write(f"{block.nonce}\n")
    f.write(f"{block.transactions}\n")
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
    f = open(f'wallet_file/%d.txt' % wallet.address, 'w')
    f.write(f"{wallet.private_key}\n")
    f.write(f"{wallet.public_key}\n")
    f.write(f"{wallet.hash_public_key}\n")
    f.write(f"{wallet.address}\n")
