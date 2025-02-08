import os
import binascii

# Генерация случайного ключа
secret_key = binascii.hexlify(os.urandom(32)).decode()

print(secret_key)