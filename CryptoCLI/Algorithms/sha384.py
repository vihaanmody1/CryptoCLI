from hashlib import sha384

def encrypt(text):
    return sha384(text.encode()).hexdigest()

