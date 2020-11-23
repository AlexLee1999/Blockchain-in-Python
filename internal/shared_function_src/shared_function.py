import hashlib
import binascii
import ecdsa
import base58


def hash_string(hstring):
    return hashlib.sha256(hstring.encode('utf-8')).hexdigest()


def gen_key():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p, hashfunc=hashlib.sha256)
    vk = sk.get_verifying_key()
    return sk.to_string().hex(), vk.to_string().hex()


def hash_public_key(public_key):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(binascii.unhexlify(public_key)).digest())
    return ripemd160.hexdigest()


def get_address(public_key_hash):
    return base58.b58encode(public_key_hash)


def pubkey_to_verifykey(pub_key, curve=ecdsa.SECP256k1):
    vk_string = binascii.unhexlify(pub_key)
    return ecdsa.VerifyingKey.from_string(vk_string, curve=curve)

