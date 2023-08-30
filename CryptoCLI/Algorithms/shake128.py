from hashlib import new

def encrypt(text):
    Shake256 = new("shake_128", text.encode())
    return Shake256.hexdigest(32)
