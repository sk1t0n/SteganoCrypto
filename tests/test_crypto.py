import unittest

import crypto


class TestCrypto(unittest.TestCase):
    def test_compare_secret_and_dec_secret(self):
        """Сравнивает исходный текст и расшифрованный текст."""

        password = 'super password'
        secret = 'super secret'
        enc_secret = crypto.encrypt(password, secret)
        dec_secret = crypto.decrypt(password, enc_secret)
        return self.assertEqual(secret, dec_secret)


if __name__ == '__main__':
    unittest.main()
