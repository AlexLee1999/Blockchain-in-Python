import internal.shared_function_src.shared_function as shared_function
import json


class txinput(object):
    def __init__(self, txid, vout, sig, public_key):
        self._txid = txid
        self._vout = vout
        self._sig = sig
        self._public_key = public_key

    def __repr__(self):
        return f"ID : {self._txid}, Vout : {self._vout}, Signature : {self._sig}, Public key : {self._public_key}"

    @property
    def txid(self):
        return self._txid

    @property
    def vout(self):
        return self._vout

    @property
    def sig(self):
        return self._sig

    @property
    def public_key(self):
        return self._public_key

    def prepare_data(self):
        return f"{self._txid}{self._vout}{self._sig}{self._public_key}"

    def hashkey(self, public_key_hash):
        return shared_function.hash_public_key(self._public_key) == public_key_hash

