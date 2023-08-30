from hashlib import new

def encrypt(text):
    Shake256 = new("shake_256", text.encode())
    return Shake256.hexdigest(64)

