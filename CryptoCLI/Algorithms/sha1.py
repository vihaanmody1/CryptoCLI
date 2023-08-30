from hashlib import sha1

def encrypt(text):
    return sha1(text.encode()).hexdigest()
