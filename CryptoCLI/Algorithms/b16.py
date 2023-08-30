from base64 import b16encode, b16decode

def encrypt(text):
    return b16encode(text.encode()).decode()

def decrypt(text):
    try:
        b16decode(text.encode()).decode()
    except Exception as Error:
        return str(Error)
    return b16decode(text.encode()).decode()
