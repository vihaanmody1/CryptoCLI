from cryptography.fernet import Fernet

def encrypt(text):
    Key = Fernet.generate_key()
    Fern = Fernet(Key)
    Token = Fern.encrypt(text.encode())
    return {
        "token":Token.decode(),
        "key":Key.decode()
    }

def decrypt(text, key):
    try:
        Fern = Fernet(key)
        Fern.decrypt(text).decode()
    except Exception as Error:
        return Error
    return Fern.decrypt(text).decode()
