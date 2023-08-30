from hashlib import blake2b

def encrypt(text):
    return blake2b(text.encode()).hexdigest()

