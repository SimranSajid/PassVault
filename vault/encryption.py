import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def load_or_generate_key():
    try:
        with open(KEY_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

def get_fernet():
    key = load_or_generate_key()
    return Fernet(key)

def encrypt_password(plain_text):
    f = get_fernet()
    return f.encrypt(plain_text.encode()).decode()

def decrypt_password(encrypted_text):
    f = get_fernet()
    try:
        return f.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return encrypted_text