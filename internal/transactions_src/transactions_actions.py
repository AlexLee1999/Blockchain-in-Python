import internal.transactions_src.transactions as transactions
import internal.transactions_src.txinput as txinput
import internal.transactions_src.txoutput as txoutput


subsidy = 50


def coinbase_transactions(to):
    data = f"Reward to {to}"
    txin = txinput.txinput("", -1, data)
    txout = txoutput.txoutput(subsidy, to)
    tx = transactions.transactions()
    tx.add_vin(txin)
    tx.add_vout(txout)
    tx.set_id()
    return tx
