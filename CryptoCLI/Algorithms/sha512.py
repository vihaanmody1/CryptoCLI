from hashlib import sha512

def encrypt(text):
    return sha512(text.encode()).hexdigest()

