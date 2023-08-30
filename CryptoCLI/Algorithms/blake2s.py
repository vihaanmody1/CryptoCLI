from hashlib import blake2s

def encrypt(text):
    return blake2s(text.encode()).hexdigest()

