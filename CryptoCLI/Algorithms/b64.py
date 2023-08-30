from base64 import b64encode, b64decode

def encrypt(text):
    return b64encode(text.encode()).decode()

def decrypt(text):
    try:
        b64decode(text.encode()).decode()
    except Exception as Error:
        return str(Error)
    return b64decode(text.encode()).decode()
