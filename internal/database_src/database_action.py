import internal.block_src.block as block
import internal.block_src.block_chain as block_chain


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
