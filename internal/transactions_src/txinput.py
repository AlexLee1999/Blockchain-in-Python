class txinput(object):
    def __init__(self, txid, vout, script_sig):
        self._txid = txid
        self._vout = vout
        self._script_sig = script_sig

    def __repr__(self):
        return f"ID : {self._txid}, Vout : {self._vout}, Script_sig : {self._script_sig}"

    @property
    def txid(self):
        return self._txid

    @property
    def vout(self):
        return self._vout
    
    @property
    def script_sig(self):
        return self._script_sig

    def prepare_data(self):
        return f"{self._txid}{self._vout}{self._script_sig}"
