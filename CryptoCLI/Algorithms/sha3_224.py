from hashlib import sha3_224

def encrypt(text):
    return sha3_224(text.encode()).hexdigest()

