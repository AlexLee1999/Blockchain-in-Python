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


def new_transactions(f, to, amount, bc, wallet_set, utxo):
    inputs = []
    outputs = []
    wallet_f = wallet_set.find_via_address(f)
    wallet_t = wallet_set.find_via_address(to)

    acc, valid_outputs = utxo.find_spendable_outputs(wallet_f.hash_public_key, amount)
    if acc < amount:
        print('Not enough funds')
        return
    for tx_id, outs in valid_outputs.items():
        for out in outs:
            input = txinput.txinput(tx_id, out, None, wallet_f.public_key)
            inputs.append(input)
    outputs.append(txoutput.txoutput(amount, wallet_t.hash_public_key))
    if acc > amount:
        outputs.append(txoutput.txoutput(acc-amount, wallet_f.hash_public_key))

    new_t = transactions.transactions()
    for out in outputs:
        new_t.add_vout(out)
    for ins in inputs:
        new_t.add_vin(ins)
    new_t.set_id()
    return new_t



