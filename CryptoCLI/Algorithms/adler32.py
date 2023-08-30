import zlib

def encrypt(text):
    return zlib.adler32(text.encode())
