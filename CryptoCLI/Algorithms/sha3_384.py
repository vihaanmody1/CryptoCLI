from hashlib import sha3_384

def encrypt(text):
    return sha3_384(text.encode()).hexdigest()

