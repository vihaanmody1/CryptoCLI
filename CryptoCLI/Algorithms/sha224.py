from hashlib import sha224

def encrypt(text):
    return sha224(text.encode()).hexdigest()

