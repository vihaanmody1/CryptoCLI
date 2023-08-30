from hashlib import md5

def encrypt(text):
    return md5(text.encode()).hexdigest()

