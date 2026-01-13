from argon2 import PasswordHasher #module de hachage
from pathlib import Path
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher() #fonction pour hash
MASTER_HASH = Path("maitre.hash")

def master_exist() -> bool:
    return MASTER_HASH.exists()

def create_master(password:str) -> None:
    return MASTER_HASH.write_text(ph.hash(password))

def verify_master(password:str) -> bool:
    stock_hash = MASTER_HASH.read_text()
    try:
        ph.verify(stock_hash, password)
        return True
    except VerifyMismatchError:
        return False






