from hashlib import new

def encrypt(text):
    Whirlpool = new("whirlpool", text.encode())
    return Whirlpool.hexdigest()

