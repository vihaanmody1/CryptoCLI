from hashlib import new

def encrypt(text):
    SM3 = new("sm3", text.encode())
    return SM3.hexdigest()

