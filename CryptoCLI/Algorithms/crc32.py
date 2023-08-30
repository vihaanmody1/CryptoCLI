import binascii

def encrypt(text):
    return binascii.crc32(text.encode())

