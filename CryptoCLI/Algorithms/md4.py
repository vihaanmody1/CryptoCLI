from hashlib import new

def encrypt(text):
    MD4 = new("md4", text.encode())
    return MD4.hexdigest()
