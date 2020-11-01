class txoutput(object):
    def __init__(self, value, script_pub_key):
        self._value = value
        self._script_pub_key = script_pub_key

    def __repr__(self):
        return f"Value : {self._value}, Script Public Key : {self._script_pub_key}"

    @property
    def value(self):
        return self._value

    @property
    def script_pub_key(self):
        return self._script_pub_key

    def get_data(self):
        return f"{self._value}{self._script_pub_key}"


