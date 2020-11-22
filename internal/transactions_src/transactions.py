import internal.shared_function_src.shared_function as shared_function
import json

class transactions(object):
    def __init__(self, id = ''):
        self._id = id
        self._vin = []
        self._vout = []

    def __repr__(self):
        string = f"ID : {self._id} "
        string += "TXin : "
        for vin in self._vin:
            string += f"({vin}) "
        string += "TXout : "
        for vout in self._vout:
            string += f"({vout}) "
        return string

    @property
    def id(self):
        return self._id

    @property
    def vin(self):
        return self._vin

    @property
    def vout(self):
        return self._vout

    def set_id(self):
        self._id = self.hash()

    def hash(self):
        string = f"{self._id}"
        for vin in self._vin:
            string += f"{vin}"
        for vout in self._vout:
            string += f"{vout}"
        return shared_function.hash_string(string)

    def add_vin(self, txin):
        self._vin.append(txin)

    def add_vout(self, txout):
        self._vout.append(txout)

    def is_coinbase(self):
        if self.vin[0].public_key == self.vin[0].sig:
            return True
        else:
            return False

    def set_json(self):
        vin = [v.set_json() for v in self._vin]
        vout = [v.set_json() for v in self._vout]
        jsonStr = json.dumps({"id":self._id, "vin": vin, "vout": vout})
        return jsonStr
