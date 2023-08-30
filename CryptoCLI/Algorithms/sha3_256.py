from hashlib import sha3_256

def encrypt(text):
    return sha3_256(text.encode()).hexdigest()

