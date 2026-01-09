from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_master_password(password: str) -> str:
    return ph.hash(password)
