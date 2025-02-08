import os
import binascii

secret_key = binascii.hexlify(os.urandom(32)).decode()

print(secret_key)
