import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(password: str, secret: str) -> bytes:
    """Зашифровывает текст паролем.

    Args:
        password (str): пароль в открытом виде
        secret (str): текст, который надо зашифровать

    Returns:
        bytes: зашифрованный текст в виде набора байтов
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
    """Расшифровывает запороленный текст.

    Args:
        password (str): пароль в открытом виде
        enc_secret (bytes): зашифрованный паролем текст

    Returns:
        str: расшифрованный текст в виде строки
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
