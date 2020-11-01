import internal.shared_function.shared_function as shared_function


class transactions(object):
    def __init__(self):
        self._id = ""
        self._vin = []
        self._vout = []
    
    @property
    def id(self):
        return self._id

    @property
    def vin(self):
        return self._vin

    @property
    def vout(self):
        return self._vin

    def set_id(self):
        self.id = self.hash()

    def hash(self):
        string = f"{self._id}"
        for vin in self._vin:
            string += f"{vin}"
        for vout in self._vout:
            string += f"{vout}"
        return shared_function.hash_string(string)

