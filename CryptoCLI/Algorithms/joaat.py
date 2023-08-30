def encrypt(text):
    hash_value = 0
    for byte in text.encode():
        hash_value += byte
        hash_value += hash_value << 10
        hash_value ^= hash_value >> 6
    hash_value += hash_value << 3
    hash_value ^= hash_value >> 11
    hash_value += hash_value << 15
    return hash_value & 0xFFFFFFFF

