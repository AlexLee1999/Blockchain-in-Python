import internal.transactions_src.transactions as transactions
import internal.transactions_src.txinput as txinput
import internal.transactions_src.txoutput as txoutput


subsidy = 50


def coinbase_transactions(to, wallet_set):
    new_wallet = wallet_set.find_via_address(to)
    print(wallet_set)
    data = f"Reward to {to}"
    txin = txinput.txinput("", -1, data, data)
    txout = txoutput.txoutput(subsidy, new_wallet.hash_public_key)
    tx = transactions.transactions()
    tx.add_vin(txin)
    tx.add_vout(txout)
    tx.set_id()
    return tx


def new_transactions(f, to, amount, bc, wallet_set):
    inputs = []
    outputs = []
    wallet_f = wallet_set.find_via_address(f)
    ava = bc.find_account_amount(wallet_f.hash_public_key)


