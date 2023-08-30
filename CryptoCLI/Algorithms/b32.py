from base64 import b32encode, b32decode

def encrypt(text):
    return b32encode(text.encode()).decode()

def decrypt(text):
    try:
        b32decode(text.encode()).decode()
    except Exception as Error:
        return str(Error)
    return b32decode(text.encode()).decode()
