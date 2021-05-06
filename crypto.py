import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(password: str, secret: str) -> bytes:
    """Encrypt text with a password.

    Args:
        password (str): a plain text password
        secret (str): a text for encryption

    Returns:
        bytes: the encrypted text as bytes
    """

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    f = Fernet(key)
    token = f.encrypt(secret.encode('utf-8'))
    b64_salt = base64.urlsafe_b64encode(salt)
    return b64_salt + token


def decrypt(password: str, enc_secret: bytes) -> str:
    """Decrypt text with a password.

    Args:
        password (str): a plain text password
        enc_secret (bytes): a encrypted text as bytes

    Returns:
        str: the decoded text as a string
    """

    salt = base64.urlsafe_b64decode(enc_secret[:24])
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    f = Fernet(key)
    secret = f.decrypt(enc_secret[24:]).decode('utf-8')
    return secret
