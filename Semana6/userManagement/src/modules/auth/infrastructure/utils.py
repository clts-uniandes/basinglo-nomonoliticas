import hashlib
from os import urandom

def encrypt_password(password):
    salt = urandom(16)
    salted_password = password.encode("utf-8") + salt
    encrypt_password = hashlib.sha256(salted_password).hexdigest()
    return encrypt_password, salt

def verify_password(hashed_password, salt, password_to_check):
    salt_cleaned = salt.replace("\\x", "")
    salt_bytes = bytes.fromhex(salt_cleaned)
    password_bytes = password_to_check.encode("utf-8")
    salted_password_to_check = password_bytes + salt_bytes
    hashed_password_to_check = hashlib.sha256(salted_password_to_check).hexdigest()
    return hashed_password_to_check == hashed_password

def get_token():
    new_token = urandom(16)
    token_hex = new_token.hex()
    return token_hex.lstrip("\\x")
