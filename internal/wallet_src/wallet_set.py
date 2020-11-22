class wallet_set(object):
    def __init__(self):
        self._wallets = []

    def add_wallet(self, wallet):
        self._wallets.append(wallet)

    def find_via_address(self, address):
        for wallet in self._wallets:
            if wallet.address == address:
                return wallet
    def __repr__(self):
        s = ""
        for wallet in self._wallets:
            s += f'{wallet}\n'
        return s
