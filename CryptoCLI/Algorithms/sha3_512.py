from hashlib import sha3_512

def encrypt(text):
    return sha3_512(text.encode()).hexdigest()

