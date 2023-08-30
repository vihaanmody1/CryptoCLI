from hashlib import sha256

def encrypt(text):
    return sha256(text.encode()).hexdigest()

