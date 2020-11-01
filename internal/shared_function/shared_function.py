import hashlib


def hash_string(hstring):
    return hashlib.sha256(hstring.encode('utf-8')).hexdigest()

