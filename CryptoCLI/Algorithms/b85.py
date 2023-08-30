from base64 import b85encode, b85decode

def encrypt(text):
    return b85encode(text.encode()).decode()

def decrypt(text):
    try:
        b85decode(text.encode()).decode()
    except Exception as Error:
        return str(Error)
    return b85decode(text.encode()).decode()
