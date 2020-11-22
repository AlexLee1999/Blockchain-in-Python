class txoutput(object):
    def __init__(self, value, public_key_hash):
        self._value = value
        self._public_key_hash = public_key_hash

    def __repr__(self):
        return f"Value : {self._value}, Public Key Hash: {self._public_key_hash}"

    @property
    def value(self):
        return self._value

    @property
    def public_key_hash(self):
        return self._public_key_hash

    def get_data(self):
        return f"{self._value}{self._public_key_hash}"


