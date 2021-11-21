from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Encryption:

    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(raw, AES.block_size))
        con = cipher.iv+ct_bytes
        return b64encode(con)

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:16]
        ct = enc[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return "the message is", pt.decode()
