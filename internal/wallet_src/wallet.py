import internal.shared_function_src.shared_function as shared_function
import os
import ecdsa
import hashlib
import binascii


class wallet(object):
    def __init__(self, private_key, public_key, hash_public_key, address):
        if private_key is None and public_key is None:
            self._private_key, self._public_key = shared_function.gen_key()
            self._hash_public_key = shared_function.hash_public_key(self._public_key)
            self._address = (shared_function.get_address(self._hash_public_key)).decode()
        else:
            self._private_key = private_key
            self._public_key = public_key
            self._hash_public_key = hash_public_key
            self._address = address

    @property
    def private_key(self):
        return self._private_key

    @property
    def public_key(self):
        return self._public_key

    @property
    def hash_public_key(self):
        return self._hash_public_key

    @property
    def address(self):
        return self._address

    def __repr__(self):
        return f"Private key : {self.private_key}, Public key : {self.public_key}, Hash public key : {self._hash_public_key}, Address : {self.address}"

