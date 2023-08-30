from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt(text):
    return urlsafe_b64encode(text.encode()).decode()

def decrypt(text):
    try:
        urlsafe_b64decode(text.encode()).decode()
    except Exception as Error:
        return str(Error)
    return urlsafe_b64decode(text.encode()).decode()
