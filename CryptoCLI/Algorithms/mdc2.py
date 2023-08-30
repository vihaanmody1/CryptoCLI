from hashlib import new

def encrypt(text):
    MDC2 = new("mdc2", text.encode())
    return MDC2.hexdigest()

