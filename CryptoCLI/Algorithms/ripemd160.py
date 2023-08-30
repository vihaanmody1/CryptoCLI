from hashlib import new

def encrypt(text):
    Ripemd160 = new("ripemd160", text.encode())
    return Ripemd160.hexdigest()
