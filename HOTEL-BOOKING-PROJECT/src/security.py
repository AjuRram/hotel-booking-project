from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
import secrets

class SecurityManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def hash_password(self, password: str, salt: bytes = None) -> tuple[str, bytes]:
        salt = salt or secrets.token_bytes(16)
        hash_bytes = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return hash_bytes.hex(), salt

    def encrypt_sensitive_data(self, data: str) -> bytes:
        return self.cipher_suite.encrypt(data.encode())

security_manager = SecurityManager()
