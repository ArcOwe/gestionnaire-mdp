import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

salt = b"gestionnaire-mdp-salt"

def derive_key(mdp_maitre: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = kdf.derive(mdp_maitre.encode())
    return base64.urlsafe_b64encode(key)

if __name__ == "__main__":
    key = derive_key("mdp_test")
    print("Clé dérivée :", key)
